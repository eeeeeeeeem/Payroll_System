# Generated by Django 5.1.2 on 2024-11-22 12:32

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Payroll', '0017_user_role'),
    ]

    operations = [
        migrations.CreateModel(
            name='TimeRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('punch_in', models.DateTimeField(auto_now_add=True)),
                ('punch_out', models.DateTimeField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='time_records', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-date', '-punch_in'],
            },
        ),
    ]
