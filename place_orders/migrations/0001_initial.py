# Generated by Django 2.2.4 on 2019-08-28 23:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='placeOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(blank=True, max_length=75)),
                ('dateCreated', models.DateField(auto_now=True)),
                ('total', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Total')),
                ('emailAddress', models.EmailField(blank=True, max_length=75, verbose_name='Email Address')),
                ('billingName', models.CharField(blank=True, max_length=75)),
                ('billingAddress', models.CharField(blank=True, max_length=75)),
                ('billingCity', models.CharField(blank=True, max_length=75)),
                ('billingPostal', models.CharField(blank=True, max_length=75)),
            ],
            options={
                'db_table': 'placeOrder',
                'ordering': ['-dateCreated'],
            },
        ),
        migrations.CreateModel(
            name='yourItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('painting', models.CharField(max_length=75)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Price')),
                ('quantity', models.IntegerField()),
                ('place_order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='place_orders.placeOrder')),
            ],
            options={
                'db_table': 'yourItem',
            },
        ),
    ]
