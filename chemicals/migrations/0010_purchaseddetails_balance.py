# Generated by Django 5.0.6 on 2024-06-12 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chemicals', '0009_purchaseddetails_bill_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchaseddetails',
            name='Balance',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
