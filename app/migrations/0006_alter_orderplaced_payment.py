# Generated by Django 4.1.5 on 2023-02-09 09:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_payment_orderplaced'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderplaced',
            name='payment',
            field=models.ForeignKey(default=' ', on_delete=django.db.models.deletion.CASCADE, to='app.payment'),
        ),
    ]
