# Generated by Django 3.0.4 on 2020-07-25 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plasma', '0002_recipient_hospital'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donars',
            name='blood',
            field=models.CharField(max_length=5),
        ),
        migrations.AlterField(
            model_name='recipient',
            name='blood',
            field=models.CharField(max_length=5),
        ),
    ]