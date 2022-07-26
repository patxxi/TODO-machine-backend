from django.contrib.auth import get_user_model

from rest_framework import generics, authentication, permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.response import Response
from rest_framework import status

from user.serializers import UserSerializer, AuthTokenSerializer
from workspace.serializers import WorkspaceSerializer
from core import models


class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        """
        It creates a new user, then creates a new workspace for that user

        :param request: The request object
        :return: The response is being returned.
        """
        response = super().create(request, *args, **kwargs)
        user = get_user_model().objects.get(id=response.data['id'])

        models.Workspace.objects.create(user=user, title='Home')
        return response


class ManageUserView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return models.User.objects.filter(id=self.request.user.id)

    def retrieve(self, request, *args, **kwargs):
        """
        It retrieves the user and all of their workspaces

        :param request: The request object
        :return: The user and the workspaces associated with that user.
        """
        user = get_user_model().objects.filter(id=request.user.id)
        user_data = UserSerializer(user, many=True)

        workspaces = models.Workspace.objects.filter(user=request.user)
        workspaces_data = WorkspaceSerializer(workspaces, many=True)

        return Response({
            'user': user_data.data[0],
            'workspaces': workspaces_data.data
        }, status=status.HTTP_200_OK)


class AuthTokenView(ObtainAuthToken):
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
