# Generated by Django 4.1.2 on 2022-11-21 01:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CaruselImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='name')),
                ('name_en', models.CharField(max_length=50, null=True, verbose_name='name')),
                ('name_uz', models.CharField(max_length=50, null=True, verbose_name='name')),
                ('name_ru', models.CharField(max_length=50, null=True, verbose_name='name')),
                ('image', models.ImageField(upload_to='media/carusel', verbose_name='image')),
            ],
            options={
                'verbose_name': 'Karusel',
            },
        ),
        migrations.CreateModel(
            name='ContactForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='name')),
                ('phone_number', models.IntegerField(verbose_name='phone_number')),
                ('description', models.TextField(max_length=550, verbose_name='description')),
            ],
            options={
                'verbose_name': 'Kontakt',
            },
        ),
        migrations.CreateModel(
            name='GallaryCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='name')),
                ('name_en', models.CharField(max_length=50, null=True, verbose_name='name')),
                ('name_uz', models.CharField(max_length=50, null=True, verbose_name='name')),
                ('name_ru', models.CharField(max_length=50, null=True, verbose_name='name')),
                ('image', models.ImageField(upload_to='media/gallary', verbose_name='image')),
            ],
            options={
                'verbose_name': 'Gallary Category',
            },
        ),
        migrations.CreateModel(
            name='OrderCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=65, verbose_name='name')),
            ],
            options={
                'verbose_name': 'Sub Order Category',
            },
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roomname', models.CharField(blank=True, max_length=100, null=True, verbose_name='roomname')),
                ('roomprice', models.IntegerField(blank=True, null=True, verbose_name='roomprice')),
                ('servicename', models.CharField(blank=True, max_length=100, null=True, verbose_name='servicename')),
                ('user_name', models.CharField(max_length=65, verbose_name='user name')),
                ('user_phone_number', models.CharField(max_length=65, verbose_name='user_phone_number')),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name='name')),
                ('name_en', models.CharField(blank=True, max_length=100, null=True, verbose_name='name')),
                ('name_uz', models.CharField(blank=True, max_length=100, null=True, verbose_name='name')),
                ('name_ru', models.CharField(blank=True, max_length=100, null=True, verbose_name='name')),
                ('price', models.PositiveIntegerField(verbose_name='price')),
            ],
            options={
                'verbose_name': 'Xona turlari',
            },
        ),
        migrations.CreateModel(
            name='Room2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name='name')),
                ('name_en', models.CharField(blank=True, max_length=100, null=True, verbose_name='name')),
                ('name_uz', models.CharField(blank=True, max_length=100, null=True, verbose_name='name')),
                ('name_ru', models.CharField(blank=True, max_length=100, null=True, verbose_name='name')),
                ('description', models.TextField(max_length=550, verbose_name='description')),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/ccc', verbose_name='image')),
            ],
            options={
                'verbose_name': 'Xona detaillari',
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=120, null=True, verbose_name='name')),
                ('name_en', models.CharField(blank=True, max_length=120, null=True, verbose_name='name')),
                ('name_uz', models.CharField(blank=True, max_length=120, null=True, verbose_name='name')),
                ('name_ru', models.CharField(blank=True, max_length=120, null=True, verbose_name='name')),
                ('price', models.PositiveIntegerField(verbose_name='price')),
            ],
            options={
                'verbose_name': 'Xizmat kursatish turlari',
            },
        ),
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=50, verbose_name='key')),
                ('value', models.CharField(max_length=500, verbose_name='value')),
            ],
            options={
                'verbose_name': 'Sozlamalar',
            },
        ),
        migrations.CreateModel(
            name='SubServices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='name')),
                ('name_en', models.CharField(max_length=50, null=True, verbose_name='name')),
                ('name_uz', models.CharField(max_length=50, null=True, verbose_name='name')),
                ('name_ru', models.CharField(max_length=50, null=True, verbose_name='name')),
                ('is_exist', models.BooleanField(default=True, verbose_name='is_exist')),
            ],
            options={
                'verbose_name': 'Sub Card Xizmatlar',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='title')),
                ('title_en', models.CharField(max_length=200, null=True, verbose_name='title')),
                ('title_uz', models.CharField(max_length=200, null=True, verbose_name='title')),
                ('title_ru', models.CharField(max_length=200, null=True, verbose_name='title')),
                ('description', models.TextField(verbose_name='description')),
                ('description_en', models.TextField(null=True, verbose_name='description')),
                ('description_uz', models.TextField(null=True, verbose_name='description')),
                ('description_ru', models.TextField(null=True, verbose_name='description')),
                ('gallary', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clining.room2')),
            ],
            options={
                'verbose_name': 'Project',
            },
        ),
        migrations.CreateModel(
            name='OrderForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='name')),
                ('email', models.EmailField(max_length=60, verbose_name='email')),
                ('phone_number', models.IntegerField(verbose_name='phone_number')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clining.ordercategory')),
            ],
            options={
                'verbose_name': 'Order Form',
            },
        ),
        migrations.CreateModel(
            name='GallaryDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='title')),
                ('title_en', models.CharField(max_length=200, null=True, verbose_name='title')),
                ('title_uz', models.CharField(max_length=200, null=True, verbose_name='title')),
                ('title_ru', models.CharField(max_length=200, null=True, verbose_name='title')),
                ('description', models.TextField(verbose_name='description')),
                ('description_en', models.TextField(null=True, verbose_name='description')),
                ('description_uz', models.TextField(null=True, verbose_name='description')),
                ('description_ru', models.TextField(null=True, verbose_name='description')),
                ('gallary', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clining.gallarycategory')),
            ],
            options={
                'verbose_name': 'Gallery Detail',
            },
        ),
        migrations.CreateModel(
            name='CaruselDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('title_en', models.CharField(max_length=255, null=True, verbose_name='title')),
                ('title_uz', models.CharField(max_length=255, null=True, verbose_name='title')),
                ('title_ru', models.CharField(max_length=255, null=True, verbose_name='title')),
                ('description', models.TextField(verbose_name='description')),
                ('description_en', models.TextField(null=True, verbose_name='description')),
                ('description_uz', models.TextField(null=True, verbose_name='description')),
                ('description_ru', models.TextField(null=True, verbose_name='description')),
                ('carusel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clining.caruselimage')),
            ],
            options={
                'verbose_name': 'Carusel Detail',
            },
        ),
        migrations.CreateModel(
            name='CardServices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('name_en', models.CharField(max_length=100, null=True, verbose_name='name')),
                ('name_uz', models.CharField(max_length=100, null=True, verbose_name='name')),
                ('name_ru', models.CharField(max_length=100, null=True, verbose_name='name')),
                ('price', models.PositiveIntegerField(verbose_name='price')),
                ('detail', models.TextField(verbose_name='detail')),
                ('detail_en', models.TextField(null=True, verbose_name='detail')),
                ('detail_uz', models.TextField(null=True, verbose_name='detail')),
                ('detail_ru', models.TextField(null=True, verbose_name='detail')),
                ('service', models.ManyToManyField(to='clining.subservices')),
            ],
            options={
                'verbose_name': 'Card Xizmatlar',
            },
        ),
    ]
