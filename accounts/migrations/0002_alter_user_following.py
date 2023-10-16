# Generated by Django 4.2.6 on 2023-10-16 14:13

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='following',
            field=models.ManyToManyField(blank=True, through='accounts.Follow', to=settings.AUTH_USER_MODEL),
        ),
    ]
