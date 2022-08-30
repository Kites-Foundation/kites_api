# Generated by Django 4.1 on 2022-08-30 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_rename_name_user_fullname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='tshirt_size',
            field=models.CharField(blank=True, choices=[('XS', 'XS'), ('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL'), ('XXL', 'XXL'), ('XXL', 'XXL')], default='', max_length=10, verbose_name='T shirt Size'),
        ),
    ]
