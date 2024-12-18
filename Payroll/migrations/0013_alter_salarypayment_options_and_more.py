# Generated by Django 5.1.1 on 2024-11-20 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Payroll', '0012_salarypayment_delete_payroll'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='salarypayment',
            options={'ordering': ['-payment_date']},
        ),
        migrations.RenameField(
            model_name='salarypayment',
            old_name='salary',
            new_name='base_salary',
        ),
        migrations.RenameField(
            model_name='salarypayment',
            old_name='end_date',
            new_name='payment_date',
        ),
        migrations.RemoveField(
            model_name='salarypayment',
            name='start_date',
        ),
        migrations.AddField(
            model_name='salarypayment',
            name='bonus',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='salarypayment',
            name='deduction',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]
