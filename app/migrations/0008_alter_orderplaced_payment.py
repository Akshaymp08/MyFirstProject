# Generated by Django 4.1.5 on 2023-02-11 16:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_wishlist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderplaced',
            name='payment',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='app.payment'),
        ),
    ]