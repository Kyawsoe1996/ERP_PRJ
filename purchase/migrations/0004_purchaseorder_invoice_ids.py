# Generated by Django 3.1.4 on 2021-08-10 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0005_invoiceline_sub_total'),
        ('purchase', '0003_remove_purchaseorderline_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchaseorder',
            name='invoice_ids',
            field=models.ManyToManyField(blank=True, to='invoice.Invoice'),
        ),
    ]
