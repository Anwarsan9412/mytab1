# Generated by Django 3.2.4 on 2021-08-08 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_rename_month_saldoawal_month'),
    ]

    operations = [
        migrations.AddField(
            model_name='pengeluaran',
            name='month',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
