# Generated by Django 5.0.2 on 2024-02-11 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='contact_number',
            field=models.CharField(default=1234567890, max_length=20),
            preserve_default=False,
        ),
    ]
