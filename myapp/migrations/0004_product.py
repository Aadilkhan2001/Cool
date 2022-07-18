# Generated by Django 3.2.6 on 2021-09-23 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_rename_product_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='demo', max_length=30)),
                ('price', models.FloatField(default=400)),
                ('desc', models.CharField(default='test', max_length=250)),
                ('image', models.ImageField(upload_to='ptimage')),
            ],
        ),
    ]