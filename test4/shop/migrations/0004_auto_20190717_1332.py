# Generated by Django 2.2.3 on 2019-07-17 05:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20190716_1746'),
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=10)),
            ],
        ),
        migrations.AlterField(
            model_name='foods',
            name='color',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Color'),
        ),
        migrations.RemoveField(
            model_name='foods',
            name='tag',
        ),
        migrations.AddField(
            model_name='foods',
            name='tag',
            field=models.ManyToManyField(to='shop.Tag'),
        ),
    ]
