# Generated by Django 4.0.6 on 2022-08-25 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_todo_completed'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='status',
            field=models.CharField(default='pending', max_length=100),
        ),
    ]
