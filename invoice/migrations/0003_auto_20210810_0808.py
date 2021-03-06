# Generated by Django 3.1.4 on 2021-08-10 08:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0002_invoice_total_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='creation_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='invoice',
            name='invoice_date',
            field=models.DateField(default=datetime.date(2021, 8, 10)),
            preserve_default=False,
        ),
    ]
