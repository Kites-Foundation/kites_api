# Generated by Django 4.1 on 2022-08-30 22:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_remove_user_achievements_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='name',
            new_name='fullname',
        ),
    ]