# Generated by Django 5.0.6 on 2024-06-28 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserFeatures', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='buyers',
            name='remaining_partitions',
        ),
        migrations.AddField(
            model_name='invoices',
            name='remaining_partitions',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
