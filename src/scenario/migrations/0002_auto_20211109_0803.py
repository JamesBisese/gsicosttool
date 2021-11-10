# Generated by Django 3.2.5 on 2021-11-09 15:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('scenario', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Create Date'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='modified_date',
            field=models.DateTimeField(auto_now=True, verbose_name='Modified Date'),
        ),
    ]
