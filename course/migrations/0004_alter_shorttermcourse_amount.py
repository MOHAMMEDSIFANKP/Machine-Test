# Generated by Django 4.2.6 on 2023-10-26 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0003_alter_shorttermcourse_subtitle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shorttermcourse',
            name='amount',
            field=models.BigIntegerField(),
        ),
    ]