# Generated by Django 4.0.4 on 2023-02-06 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0007_alter_stock_maximum_quantity_alter_stock_quantity_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='maximum_quantity',
            field=models.CharField(blank=True, default=None, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='quantity',
            field=models.CharField(blank=True, default=None, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='reorder_quantity',
            field=models.CharField(blank=True, default=None, max_length=20, null=True),
        ),
    ]