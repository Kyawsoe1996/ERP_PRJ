# Generated by Django 3.1.4 on 2021-08-16 12:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_auto_20210804_1240'),
    ]

    operations = [
        migrations.AddField(
            model_name='productcategory',
            name='category_parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='product.productcategory'),
        ),
    ]