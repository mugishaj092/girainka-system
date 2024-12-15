# Generated by Django 5.1.3 on 2024-12-12 10:24

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cows', '0001_initial'),
        ('members', '0003_user_verified'),
    ]

    operations = [
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('province', models.CharField(max_length=255)),
                ('district', models.CharField(max_length=255)),
                ('sector', models.CharField(max_length=255)),
                ('cell', models.CharField(max_length=255)),
                ('village', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'sources',
            },
        ),
        migrations.AddField(
            model_name='cow',
            name='birthdate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='cow',
            name='giver_Id',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='given_cow', to='members.user'),
        ),
        migrations.AddField(
            model_name='cow',
            name='giver_away_Id',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cow_given_away', to='members.user'),
        ),
        migrations.AddField(
            model_name='cow',
            name='reason',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='cow',
            name='status',
            field=models.CharField(choices=[('healthy', 'Healthy'), ('sick', 'Sick'), ('dead', 'Dead')], default='healthy', max_length=10),
        ),
        migrations.AlterField(
            model_name='cow',
            name='owner',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='owned_cow', to='members.user'),
        ),
        migrations.AlterModelTable(
            name='cow',
            table='cows',
        ),
        migrations.AddField(
            model_name='cow',
            name='source',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cows', to='cows.source'),
        ),
    ]
