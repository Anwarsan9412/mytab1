# Generated by Django 3.2.4 on 2021-08-05 05:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20210801_1301'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Tabungan',
            new_name='SaldoAwal',
        ),
        migrations.CreateModel(
            name='Pengeluaran',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nominal', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('keperluan', models.CharField(max_length=100)),
                ('tanggal', models.DateField(auto_now=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('nama', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.profile')),
            ],
        ),
    ]