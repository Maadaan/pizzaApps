# Generated by Django 3.0.8 on 2020-07-18 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzaapp', '0003_ordermodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordermodel',
            name='status',
            field=models.CharField(default='pending', max_length=20),
            preserve_default=False,
        ),
    ]
