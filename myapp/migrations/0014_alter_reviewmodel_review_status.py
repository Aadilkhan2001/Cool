# Generated by Django 4.0.1 on 2022-01-23 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0013_alter_customermodel_mobile_reviewmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviewmodel',
            name='review_status',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4)], default=1, max_length=10),
        ),
    ]