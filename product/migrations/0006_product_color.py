# Generated by Django 3.1.4 on 2022-02-01 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_product_vendor'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='color',
            field=models.CharField(blank=True, choices=[('red', 'RED'), ('green', 'GREEN'), ('black', 'BLACK'), ('yellow', 'YELLOW'), ('silver', 'SILVER')], default='red', max_length=10, null=True),
        ),
    ]
