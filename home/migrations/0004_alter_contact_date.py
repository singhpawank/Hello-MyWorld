# Generated by Django 3.2.8 on 2021-10-27 18:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_contact_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
