# Generated by Django 2.2 on 2023-01-07 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Resources', '0005_newsalert'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsalert',
            name='Name',
            field=models.CharField(max_length=200, null=True),
        ),
    ]