# Generated by Django 5.0.2 on 2024-02-11 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='status',
            field=models.CharField(default='OPEN', max_length=20),
        ),
    ]
