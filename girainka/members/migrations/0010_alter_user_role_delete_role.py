# Generated by Django 5.1.3 on 2024-12-15 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0009_alter_user_managers_remove_user_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('citizen', 'Citizen'), ('admin', 'Admin')], default='citizen', max_length=10),
        ),
        migrations.DeleteModel(
            name='Role',
        ),
    ]