# Generated by Django 3.2.6 on 2021-12-13 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_alter_productmodels_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodels',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
