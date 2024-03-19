# Generated by Django 4.2.11 on 2024-03-15 23:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('date_from', models.DateTimeField(blank=True, null=True)),
                ('date_until', models.DateTimeField(blank=True, null=True)),
                ('details', models.CharField(max_length=500)),
                ('location', models.CharField(choices=[('cork', 'Cork'), ('dublin', 'Dublin'), ('kerry', 'Kerry')], default='cork', max_length=50)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='schedules', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-creation_date'],
            },
        ),
    ]
