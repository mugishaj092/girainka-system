# Generated by Django 5.1.3 on 2024-12-12 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0005_alter_user_table'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='name',
            new_name='firstName',
        ),
        migrations.AddField(
            model_name='user',
            name='lastName',
            field=models.CharField(default='unkown', max_length=255),
            preserve_default=False,
        ),
    ]
