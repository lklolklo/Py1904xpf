# Generated by Django 2.2.3 on 2019-07-03 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booktest', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='pud_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
