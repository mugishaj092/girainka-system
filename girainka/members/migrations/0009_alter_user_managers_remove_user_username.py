# Generated by Django 5.1.3 on 2024-12-15 04:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0008_alter_user_password'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='username',
        ),
    ]
