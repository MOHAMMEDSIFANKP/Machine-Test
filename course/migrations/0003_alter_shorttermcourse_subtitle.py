# Generated by Django 4.2.6 on 2023-10-26 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_shorttermcourse'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shorttermcourse',
            name='subtitle',
            field=models.CharField(max_length=100),
        ),
    ]