# Generated by Django 4.0.4 on 2022-04-24 08:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0007_alter_customer_gender'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carcompany',
            name='dealer',
        ),
        migrations.AddField(
            model_name='carcompany',
            name='Manufacture',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='car_company', to='company.manufacture'),
        ),
        migrations.AlterField(
            model_name='manufacture',
            name='dealer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='manufacture', to='company.dealer'),
        ),
    ]
