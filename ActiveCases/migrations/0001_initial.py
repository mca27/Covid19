# Generated by Django 2.0.13 on 2020-04-14 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IndiaCases',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state_name', models.CharField(max_length=250)),
                ('confirmed_Cases', models.IntegerField()),
                ('active_cases', models.IntegerField()),
                ('recovered', models.IntegerField()),
                ('deaths', models.IntegerField()),
            ],
        ),
    ]
