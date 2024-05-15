# Generated by Django 5.0.4 on 2024-05-11 14:11

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=254)),
                ('number', models.IntegerField(null=True)),
                ('city', models.CharField(max_length=150)),
                ('postal_code', models.CharField(max_length=150, verbose_name='postalCode')),
            ],
            options={
                'ordering': ['postal_code'],
            },
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoice_number', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ['invoice_number'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='productName')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('currency', models.CharField(choices=[('€', 'Eur'), ('$', 'Usd')], default='€', max_length=3)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(verbose_name='creationDate')),
                ('last_update', models.DateTimeField(verbose_name='lastUpdate')),
                ('version', models.IntegerField(default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='packtDjangoApp.address')),
                ('invoices', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='packtDjangoApp.invoice')),
            ],
            options={
                'ordering': ['user'],
            },
        ),
        migrations.AddField(
            model_name='invoice',
            name='products',
            field=models.ManyToManyField(to='packtDjangoApp.product'),
        ),
    ]
