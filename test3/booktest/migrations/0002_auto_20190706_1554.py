# Generated by Django 2.2.3 on 2019-07-06 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booktest', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hero',
            name='gender',
            field=models.CharField(choices=[('man', '男'), ('women', '女')], max_length=5),
        ),
    ]