# Generated by Django 3.0.4 on 2020-03-15 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_apartment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apartment',
            name='added_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
