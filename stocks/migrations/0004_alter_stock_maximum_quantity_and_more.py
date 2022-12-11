# Generated by Django 4.1 on 2022-11-02 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("stocks", "0003_alter_stock_maximum_quantity_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="stock",
            name="maximum_quantity",
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name="stock",
            name="reorder_quantity",
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
    ]