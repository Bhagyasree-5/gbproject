# Generated by Django 5.0.6 on 2024-06-12 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chemicals', '0010_purchaseddetails_balance'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchaseddetails',
            name='Balance',
        ),
        migrations.AddField(
            model_name='chemicals',
            name='Balance',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
