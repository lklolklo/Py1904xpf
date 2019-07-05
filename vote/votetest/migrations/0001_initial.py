# Generated by Django 2.2.3 on 2019-07-04 12:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ques',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=20)),
                ('option1', models.CharField(default='None', max_length=10)),
                ('option2', models.CharField(default='None', max_length=10)),
                ('option3', models.CharField(default='None', max_length=10)),
                ('option4', models.CharField(default='None', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Count',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('opt1', models.DecimalField(decimal_places=0, default=0, max_digits=3)),
                ('opt2', models.DecimalField(decimal_places=0, default=0, max_digits=3)),
                ('opt3', models.DecimalField(decimal_places=0, default=0, max_digits=3)),
                ('opt4', models.DecimalField(decimal_places=0, default=0, max_digits=3)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='votetest.Ques')),
            ],
        ),
    ]