# Generated by Django 4.2.4 on 2023-08-25 08:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_remove_user_mail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='city',
        ),
        migrations.RemoveField(
            model_name='user',
            name='country',
        ),
        migrations.RemoveField(
            model_name='user',
            name='education',
        ),
        migrations.RemoveField(
            model_name='user',
            name='occupation',
        ),
    ]