# Generated by Django 3.2.4 on 2021-09-04 09:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_rename_tanggal1_bayar_tanggal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='saldoawal',
            name='nama',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.profile'),
        ),
    ]