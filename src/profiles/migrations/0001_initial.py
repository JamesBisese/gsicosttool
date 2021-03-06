# Generated by Django 2.2.6 on 2020-01-25 20:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authtools', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('slug', models.UUIDField(blank=True, default=uuid.uuid4, editable=False)),
                ('user_type', models.CharField(blank=True, choices=[('standard', 'Standard user – educational purposes only'), ('professional', 'Professional user – for use with City of Raleigh design review (requires City approval)')], max_length=20, null=True, verbose_name='User Type')),
                ('favoriteDate', models.DateField(blank=True, null=True, verbose_name='Favorite Date')),
                ('picture', models.ImageField(blank=True, null=True, upload_to='profile_pics/%Y-%m-%d/', verbose_name='Profile picture')),
                ('bio', models.CharField(blank=True, max_length=200, null=True, verbose_name='Short Bio')),
                ('email_verified', models.BooleanField(default=False, verbose_name='Email verified')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
