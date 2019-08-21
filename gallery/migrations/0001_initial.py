# Generated by Django 2.2.4 on 2019-08-21 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Painting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=75, unique=True)),
                ('slug', models.SlugField(max_length=75, unique=True)),
                ('available', models.BooleanField(default=True)),
                ('quantity', models.IntegerField()),
                ('image', models.ImageField(upload_to='Painting')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField(blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'painting',
                'verbose_name_plural': 'paintings',
                'ordering': ('title',),
            },
        ),
        migrations.CreateModel(
            name='Style',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=75, unique=True)),
                ('slug', models.SlugField(max_length=75, unique=True)),
                ('description', models.TextField(blank=True)),
            ],
            options={
                'verbose_name': 'style',
                'verbose_name_plural': 'styles',
                'ordering': ('name',),
            },
        ),
    ]
