# Generated by Django 3.2.6 on 2021-09-23 13:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20210922_2035'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Product',
            new_name='Category',
        ),
    ]
