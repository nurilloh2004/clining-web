# Generated by Django 4.1.2 on 2022-11-21 00:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clining', '0006_alter_room_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='room',
            options={'verbose_name': 'Xona turlari'},
        ),
        migrations.AlterModelOptions(
            name='room2',
            options={'verbose_name': 'Xona detaillari'},
        ),
    ]