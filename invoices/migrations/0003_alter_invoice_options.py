from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('invoices', '0002_alter_invoice_validity'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='invoice',
            options={},
        ),
    ]
