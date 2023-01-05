# Generated by Django 4.0.7 on 2023-01-04 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('duration', models.DateField()),
                ('value', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]