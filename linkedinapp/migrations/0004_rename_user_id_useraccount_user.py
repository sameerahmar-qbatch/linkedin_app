# Generated by Django 4.0.4 on 2022-05-23 11:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('linkedinapp', '0003_remove_useraccount_email_remove_useraccount_password_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='useraccount',
            old_name='user_id',
            new_name='user',
        ),
    ]
