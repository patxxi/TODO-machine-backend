# Generated by Django 4.0.6 on 2022-08-26 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_todo_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='title',
            field=models.CharField(default='Title', max_length=255),
        ),
    ]
