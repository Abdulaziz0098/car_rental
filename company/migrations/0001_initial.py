# Generated by Django 4.0.4 on 2022-04-23 14:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarCompany',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=100)),
                ('num_of_car_model', models.IntegerField()),
                ('volume_of_production', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='CarModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_name', models.CharField(max_length=100)),
                ('model_year', models.DateField()),
                ('body_type', models.CharField(max_length=100)),
                ('image', models.TextField()),
                ('rent_amount', models.IntegerField(default=0)),
                ('car_company', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='vehicle_car', to='company.carcompany')),
            ],
        ),
        migrations.CreateModel(
            name='CarOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('power', models.CharField(help_text='km/h', max_length=100)),
                ('battery_capacity', models.CharField(help_text='KW', max_length=100)),
                ('color', models.CharField(choices=[('White', 'White'), ('Black', 'Black'), ('Gray', 'Gray'), ('Red', 'Red'), ('Blue', 'Blue')], max_length=100)),
                ('interior_material', models.CharField(choices=[('Cloth', 'Cloth'), ('Leather', 'Leather')], max_length=100)),
                ('size_of_wheel', models.CharField(choices=[('18', '18'), ('19', '19')], max_length=100)),
                ('number_of_engine', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3')], max_length=100)),
                ('car_model', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='company.carmodel')),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=100, unique=True)),
                ('tin', models.CharField(max_length=100)),
                ('number_of_employee', models.IntegerField()),
                ('number_of_inventory', models.IntegerField(blank=True, default=0, help_text='leave it blank', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('text', models.TextField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('dob', models.DateField()),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=100)),
                ('passport', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=100)),
                ('insurance', models.CharField(max_length=100)),
                ('licence', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Dealer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dealer_name', models.CharField(max_length=100)),
                ('supply_rate', models.FloatField()),
                ('dealer_location', models.TextField(max_length=100)),
                ('company', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='company.company')),
            ],
        ),
        migrations.CreateModel(
            name='Fine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fine_cases', models.CharField(max_length=100)),
                ('fine_amount', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_of_inventory', models.CharField(choices=[('Indoor', 'Indoor'), ('Outdoor', 'Outdoor')], max_length=100)),
                ('capacity', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('company', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='company.company')),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plate_number', models.CharField(max_length=100, null=True, unique=True)),
                ('vin_number', models.CharField(max_length=100, null=True, unique=True)),
                ('inventory', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='company.inventory')),
            ],
        ),
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField()),
                ('vehicle', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='company.vehicle')),
            ],
        ),
        migrations.CreateModel(
            name='PaymentMethod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_type', models.CharField(choices=[('Visa', 'Visa'), ('Mastercard', 'Mastercard'), ('PayPal', 'PayPal')], max_length=100)),
                ('amount', models.FloatField()),
                ('card_number', models.CharField(max_length=100, null=True)),
                ('cvv', models.CharField(max_length=10, null=True)),
                ('start_day', models.DateTimeField(null=True)),
                ('end_day', models.DateTimeField(null=True)),
                ('total_day', models.CharField(max_length=10, null=True)),
                ('car', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='company.caroption')),
                ('customer', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='company.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Manufacture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manufacture_name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('num_of_car_company', models.IntegerField()),
                ('dealer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='company.dealer')),
            ],
        ),
        migrations.CreateModel(
            name='Damaged',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_option', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='company.caroption')),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='company.customer')),
                ('fine', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='company.fine')),
            ],
        ),
        migrations.AddField(
            model_name='carmodel',
            name='vehicle',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='vehicle_car', to='company.vehicle'),
        ),
        migrations.AddField(
            model_name='carcompany',
            name='dealer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='company.manufacture'),
        ),
    ]
