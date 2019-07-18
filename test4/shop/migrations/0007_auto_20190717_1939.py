# Generated by Django 2.2.3 on 2019-07-17 11:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_cart'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='foods',
        ),
        migrations.AddField(
            model_name='cart',
            name='foods',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='shop.Foods'),
        ),
    ]