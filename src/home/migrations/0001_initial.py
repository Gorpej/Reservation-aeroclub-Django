# Generated by Django 4.1.1 on 2022-10-21 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Slot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True)),
                ('start_times', models.IntegerField(blank=True)),
                ('end_times', models.IntegerField(blank=True)),
            ],
        ),
    ]