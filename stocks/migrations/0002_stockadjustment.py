# Generated by Django 4.0.4 on 2023-01-12 01:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('stocks', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StockAdjustment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('current_quantity', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='old_quantity', to='stocks.stock')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='stock_adjustments', to='stocks.stock')),
                ('new_quantity', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='new_quantity', to='stocks.stock')),
            ],
        ),
    ]