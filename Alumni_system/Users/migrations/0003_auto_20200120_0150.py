# Generated by Django 3.0.2 on 2020-01-19 20:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0002_alumni_user_is_active'),
    ]

    operations = [
        migrations.RenameField(
            model_name='alumni_user',
            old_name='is_active',
            new_name='email_is_active',
        ),
    ]