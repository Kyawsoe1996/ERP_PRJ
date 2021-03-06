# Generated by Django 3.1.4 on 2021-08-09 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchase', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchaseorder',
            name='total_price',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='purchaseorderline',
            name='price',
            field=models.FloatField(default=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='purchaseorderline',
            name='sub_total',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
