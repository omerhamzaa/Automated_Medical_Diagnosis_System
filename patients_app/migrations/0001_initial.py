# Generated by Django 5.1.2 on 2024-10-30 13:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Patients',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('symptoms', models.CharField(max_length=500)),
                ('medical_history', models.CharField(max_length=500)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('userprofile_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users_app.userprofile')),
            ],
        ),
    ]
