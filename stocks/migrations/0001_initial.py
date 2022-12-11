# Generated by Django 4.1 on 2022-10-31 14:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="DrugClass",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "created_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "ordering": ("name",),
            },
        ),
        migrations.CreateModel(
            name="Stock",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=20)),
                (
                    "maximum_quantity",
                    models.CharField(
                        blank=True, default=None, max_length=20, null=True
                    ),
                ),
                (
                    "reorder_quantity",
                    models.CharField(
                        blank=True, default=None, max_length=20, null=True
                    ),
                ),
                (
                    "shelf_number",
                    models.CharField(
                        blank=True, default=None, max_length=20, null=True
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        blank=True,
                        choices=[("Active", "active"), ("Inactive", "inactive")],
                        default=None,
                        max_length=20,
                        null=True,
                    ),
                ),
                ("deleted", models.BooleanField(default=False)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "created_by",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "item_class",
                    models.ForeignKey(
                        blank=True,
                        default=None,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="stocks.drugclass",
                    ),
                ),
            ],
            options={
                "ordering": ("name",),
            },
        ),
    ]