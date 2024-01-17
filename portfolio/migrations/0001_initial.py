# Generated by Django 5.0.1 on 2024-01-17 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bank_Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Equity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticker', models.CharField(max_length=10)),
                ('shares', models.PositiveIntegerField()),
                ('average_price_per_share', models.DecimalField(decimal_places=2, max_digits=10)),
                ('current_price_per_share', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date_purchased', models.DateField()),
            ],
        ),
    ]
