# Generated by Django 2.2.2 on 2019-06-23 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viewcrud', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.CharField(max_length=300),
        ),
    ]
