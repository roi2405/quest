# Generated by Django 4.2.4 on 2023-08-13 20:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_user_mail_alter_user_user_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='user_id',
        ),
    ]
