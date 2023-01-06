# Generated by Django 4.0.7 on 2023-01-06 14:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('suppliers', '0001_initial'),
        ('contracts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoice_number', models.CharField(max_length=10)),
                ('value', models.DecimalField(decimal_places=2, max_digits=8)),
                ('description', models.CharField(max_length=140)),
                ('verified', models.BooleanField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('validity', models.DateField()),
                ('contract', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invoices', to='contracts.contract')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invoices', to=settings.AUTH_USER_MODEL)),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invoices', to='suppliers.supplier')),
            ],
        ),
    ]
