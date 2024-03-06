# Generated by Django 4.2.4 on 2023-10-22 15:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('booking_app', '0002_remove_booking_flight_booking_departure_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='card_number',
            field=models.CharField(max_length=16, null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='cvv',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='departure_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='destination',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='expiration_date',
            field=models.CharField(max_length=7, null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='flight_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='return_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='source',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
