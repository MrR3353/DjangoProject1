# Generated by Django 3.2.4 on 2022-12-24 07:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20221222_1053'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('category', models.CharField(max_length=50, verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Работник',
                'verbose_name_plural': 'Работники',
                'db_table': 'Employer',
            },
        ),
        migrations.AlterField(
            model_name='blog',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2022, 12, 24, 10, 2, 43, 829695), verbose_name='Опубликована'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2022, 12, 24, 10, 2, 43, 830692), verbose_name='Дата комментария'),
        ),
    ]