# Generated by Django 5.1.3 on 2024-12-22 17:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Taom otini kiriting')),
                ('description', models.TextField(verbose_name='Taom haqida malumot')),
                ('photo', models.ImageField(upload_to='Dish/', verbose_name='Taom Rasmi')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='new.category', verbose_name='Kategoriyani tanglang')),
            ],
            options={
                'verbose_name': 'Ovqat',
                'verbose_name_plural': 'Ovqatlar',
                'ordering': ['-pk'],
            },
        ),
    ]
