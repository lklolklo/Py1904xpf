# Generated by Django 2.2.3 on 2019-07-19 01:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_delete_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('content', models.TextField()),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Foods')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.PollsUser')),
            ],
        ),
    ]
