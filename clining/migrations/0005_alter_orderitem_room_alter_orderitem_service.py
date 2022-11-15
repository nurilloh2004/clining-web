# Generated by Django 4.1.2 on 2022-11-14 11:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("clining", "0004_alter_order_total"),
    ]

    operations = [
        migrations.AlterField(
            model_name="orderitem",
            name="room",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="order_one_room",
                to="clining.room",
            ),
        ),
        migrations.AlterField(
            model_name="orderitem",
            name="service",
            field=models.ManyToManyField(to="clining.service"),
        ),
    ]
