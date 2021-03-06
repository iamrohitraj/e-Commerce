# Generated by Django 4.0.4 on 2022-05-01 09:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('basic', '0002_auto_20220419_0505'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=60, null=True)),
                ('quantity', models.IntegerField(blank=True, null=True)),
                ('net_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('image', models.ImageField(blank=True, default='cart/cart.png', null=True, upload_to='cart')),
                ('time', models.DateTimeField(default=django.utils.timezone.now)),
                ('buyer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='buyer1', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_id', models.CharField(blank=True, max_length=60, null=True)),
                ('title', models.CharField(blank=True, max_length=60, null=True)),
                ('quantity', models.IntegerField(blank=True, null=True)),
                ('net_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('image', models.ImageField(blank=True, default='cart/cart.png', null=True, upload_to='cart')),
                ('time', models.DateTimeField(default=django.utils.timezone.now)),
                ('buyer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='buyer', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50, null=True)),
                ('brand_name', models.CharField(blank=True, max_length=50, null=True)),
                ('content', models.TextField(blank=True, null=True)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True)),
                ('posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('image', models.ImageField(blank=True, default='products/def_post.jpeg', null=True, upload_to='products')),
                ('username', models.CharField(blank=True, max_length=100, null=True)),
                ('units_sold', models.IntegerField(blank=True, null=True)),
                ('total_reviews', models.IntegerField(blank=True, null=True)),
                ('review_likes', models.IntegerField(blank=True, null=True)),
                ('seller', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-posted',),
            },
        ),
        migrations.DeleteModel(
            name='Checkup',
        ),
        migrations.DeleteModel(
            name='Consulting',
        ),
        migrations.AddField(
            model_name='orders',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product', to='basic.products'),
        ),
        migrations.AddField(
            model_name='orders',
            name='seller',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='seller', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='cart',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product1', to='basic.products'),
        ),
        migrations.AddField(
            model_name='cart',
            name='seller',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='seller1', to=settings.AUTH_USER_MODEL),
        ),
    ]
