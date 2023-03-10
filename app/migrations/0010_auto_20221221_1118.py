# Generated by Django 3.2.4 on 2022-12-21 08:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20221221_1113'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(verbose_name='ID пользователя')),
                ('product_id', models.IntegerField(verbose_name='ID продукта')),
                ('count', models.IntegerField(verbose_name='Количество')),
                ('price', models.FloatField(verbose_name='Цена')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
                'db_table': 'Order',
            },
        ),
        migrations.AlterField(
            model_name='blog',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2022, 12, 21, 11, 18, 1, 238658), verbose_name='Опубликована'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2022, 12, 21, 11, 18, 1, 239634), verbose_name='Дата комментария'),
        ),
    ]
