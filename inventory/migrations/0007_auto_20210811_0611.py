# Generated by Django 3.1.4 on 2021-08-11 06:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_auto_20210804_1240'),
        ('inventory', '0006_stock_product_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='product_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='stocks', to='product.product'),
        ),
    ]
