# Generated by Django 3.2.7 on 2023-10-16 16:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0002_alter_message_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='user',
        ),
    ]