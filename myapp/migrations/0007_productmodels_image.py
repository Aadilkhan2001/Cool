# Generated by Django 3.2.6 on 2021-12-08 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_auto_20211205_2034'),
    ]

    operations = [
        migrations.AddField(
            model_name='productmodels',
            name='image',
            field=models.ImageField(blank=True, upload_to='ptimage'),
        ),
    ]
