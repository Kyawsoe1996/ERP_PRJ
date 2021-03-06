# Generated by Django 3.1.4 on 2021-08-26 14:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0004_auto_20210826_1424'),
        ('sale', '0006_remove_saleorderline_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='saleorder',
            name='billing_address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='billing_address', to='customer.addr'),
        ),
        migrations.AddField(
            model_name='saleorder',
            name='shipping_address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='shipping_address', to='customer.addr'),
        ),
    ]
