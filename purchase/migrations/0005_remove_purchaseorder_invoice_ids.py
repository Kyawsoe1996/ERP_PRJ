# Generated by Django 3.1.4 on 2021-08-10 09:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('purchase', '0004_purchaseorder_invoice_ids'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchaseorder',
            name='invoice_ids',
        ),
    ]
