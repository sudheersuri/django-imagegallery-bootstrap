# Generated by Django 3.0.4 on 2020-05-18 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0002_auto_20200518_1144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artistimages',
            name='user',
            field=models.CharField(default='Surya Vamshi', max_length=20),
        ),
    ]