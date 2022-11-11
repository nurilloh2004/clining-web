# Generated by Django 4.1.2 on 2022-11-11 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Orders",
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
                ("roomname", models.CharField(max_length=100)),
                ("roomprice", models.PositiveIntegerField()),
                ("servicename", models.CharField(max_length=100)),
                ("serviceprice", models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="RoomCategory",
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
                ("name", models.CharField(blank=True, max_length=100, null=True)),
                ("price", models.PositiveIntegerField()),
            ],
            options={
                "verbose_name": "Xona turlari",
            },
        ),
        migrations.CreateModel(
            name="ServiceType",
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
                ("name", models.CharField(blank=True, max_length=120, null=True)),
                ("price", models.PositiveIntegerField()),
            ],
            options={
                "verbose_name": "ServiceType",
            },
        ),
    ]