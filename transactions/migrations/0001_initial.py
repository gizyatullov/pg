# Generated by Django 4.0.4 on 2022-06-13 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_asset', models.CharField(blank=True, db_index=True, max_length=64, verbose_name='Название')),
                ('ticker', models.CharField(db_index=True, max_length=64, verbose_name='Тикер')),
                ('purchase_price', models.PositiveIntegerField(verbose_name='Цена покупки в рублях за 1 ед.')),
                ('sale_price', models.PositiveIntegerField(blank=True, null=True, verbose_name='Цена продажи в рублях за 1 ед.')),
                ('quantity', models.PositiveIntegerField(verbose_name='Количество единиц')),
                ('type_transaction', models.CharField(choices=[('L', 'покупка'), ('S', 'продажа')], default='L', max_length=1, verbose_name='Тип сделки')),
                ('tool_type', models.CharField(choices=[('S', 'акция'), ('B', 'облигация'), ('C', 'валюта')], default='S', max_length=1, verbose_name='Тип инструмента')),
                ('tax', models.PositiveSmallIntegerField(default=13, verbose_name='% налог на прибыль')),
                ('broker_exchange_commission_percentage', models.DecimalField(decimal_places=2, default=0.06, max_digits=3, verbose_name='Комиссия брокера и биржи %')),
                ('description', models.TextField(blank=True, verbose_name='Описание сделки')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата создания записи')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата редактирования записи')),
            ],
            options={
                'verbose_name': 'сделка',
                'verbose_name_plural': 'сделки',
                'ordering': ('-created_at',),
            },
        ),
    ]
