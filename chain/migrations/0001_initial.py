# Generated by Django 5.0.1 on 2024-01-12 08:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email')),
                ('country', models.CharField(max_length=100, verbose_name='страна')),
                ('city', models.CharField(max_length=100, verbose_name='город')),
                ('street', models.CharField(max_length=200, verbose_name='улица')),
                ('building', models.CharField(max_length=100, verbose_name='номер дома')),
            ],
            options={
                'verbose_name': 'Контакт',
                'verbose_name_plural': 'Контакты',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='название')),
                ('model', models.CharField(max_length=100, verbose_name='модель')),
                ('release_date', models.DateField(verbose_name='дата выхода продукта на рынок')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
            },
        ),
        migrations.CreateModel(
            name='RetailChain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='название')),
                ('type', models.CharField(choices=[('FACTORY', 'Завод'), ('RETAIL_NET', 'Розничная сеть'), ('IND_ENTREPRENEUR', 'ИП')], max_length=50, verbose_name='тип компании')),
                ('debt', models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name='задолженность')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='время создания')),
                ('contacts', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chain.contacts', verbose_name='контакты')),
                ('products', models.ManyToManyField(blank=True, null=True, to='chain.product', verbose_name='продукты')),
                ('provider', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='chain.retailchain', verbose_name='поставщик')),
            ],
            options={
                'verbose_name': 'Розничная сеть',
                'verbose_name_plural': 'Розничные сети',
            },
        ),
    ]