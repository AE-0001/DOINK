# Generated by Django 4.1.4 on 2022-12-14 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iProcessing', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='img',
            field=models.ImageField(upload_to='processing_img'),
        ),
    ]
