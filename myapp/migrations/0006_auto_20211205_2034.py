# Generated by Django 3.2.6 on 2021-12-05 15:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myapp', '0005_category_image1'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='CustomerModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('mobile', models.IntegerField(max_length=10)),
                ('add1', models.CharField(max_length=200)),
                ('add2', models.CharField(max_length=200)),
                ('ccname', models.CharField(max_length=200)),
                ('cc_add', models.CharField(max_length=200)),
                ('country', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=70)),
                ('city', models.CharField(max_length=50)),
                ('zip_code', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MaincategoryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('image', models.ImageField(blank=True, null=True, upload_to='macteimage')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('quantity', models.PositiveBigIntegerField()),
                ('status', models.CharField(choices=[('pending', 'pending'), ('Accepted', 'Accepted'), ('Packing', 'Packing'), ('Shipping', 'Shipping'), ('Delevered', 'Delevered')], default='pending', max_length=30)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.customermodel')),
            ],
        ),
        migrations.CreateModel(
            name='ProductModels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('og_price', models.FloatField(default=0)),
                ('discount', models.FloatField(default=0)),
                ('sell_price', models.FloatField(default=0)),
                ('discounted_price', models.FloatField(default=0)),
                ('status', models.CharField(choices=[('Fresh', 'Fresh'), ('New Arrival', 'New Arrival'), ('Trending', 'Trending'), ('OutofStock', 'OutofStock')], default='New Arrival', max_length=50)),
                ('m_cate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.maincategorymodel')),
            ],
        ),
        migrations.CreateModel(
            name='SubcategoryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('image', models.ImageField(blank=True, null=True, upload_to='scateimage')),
                ('mcate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.maincategorymodel')),
            ],
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.AddField(
            model_name='productmodels',
            name='s_cate',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.subcategorymodel'),
        ),
        migrations.AddField(
            model_name='order',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.productmodels'),
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='cart',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.productmodels'),
        ),
        migrations.AddField(
            model_name='cart',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
