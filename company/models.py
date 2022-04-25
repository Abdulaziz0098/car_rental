from django.db import models
from django.db.models import F


class Company(models.Model):
    company_name = models.CharField(max_length=100, unique=True)
    tin = models.CharField(max_length=100)
    number_of_employee = models.IntegerField()
    number_of_inventory = models.IntegerField(null=True, blank=True, default=0, help_text='leave it blank')

    def __str__(self):
        return str(self.company_name)


class Dealer(models.Model):
    company = models.ForeignKey(Company, null=True, on_delete=models.SET_NULL)
    dealer_name = models.CharField(max_length=100)
    supply_rate = models.FloatField()
    dealer_location = models.TextField(max_length=100)

    def __str__(self):
        return str(self.dealer_name)


class Manufacture(models.Model):
    dealer = models.ForeignKey(Dealer, null=True, on_delete=models.SET_NULL, related_name='manufacture')
    manufacture_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    num_of_car_company = models.IntegerField()

    def __str__(self):
        return str(self.manufacture_name)


class CarCompany(models.Model):
    manufacture = models.ForeignKey(Manufacture, null=True, on_delete=models.SET_NULL, related_name='car_company')
    company_name = models.CharField(max_length=100)
    num_of_car_model = models.IntegerField()
    volume_of_production = models.IntegerField()

    def __str__(self):
        return str(self.company_name)


class Inventory(models.Model):
    type = (
        ('Indoor', 'Indoor'),
        ('Outdoor', 'Outdoor'),
    )
    company = models.ForeignKey(Company, null=True, on_delete=models.SET_NULL)
    type_of_inventory = models.CharField(max_length=100, choices=type)
    capacity = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        created = self.pk is None
        super(Inventory, self).save(*args, **kwargs)
        print(2)
        if created:
            print(1)
            Company.objects.filter(company_name=self.company).update(
                number_of_inventory=F('number_of_inventory') + 1)

    def __str__(self):
        return str(self.location)


class Vehicle(models.Model):
    inventory = models.ForeignKey(Inventory, null=True, on_delete=models.SET_NULL)
    plate_number = models.CharField(max_length=100, unique=True, null=True)
    vin_number = models.CharField(max_length=100, unique=True, null=True)

    def __str__(self):
        return str(self.vin_number) + ' -|- ' + str(self.plate_number)


class Sales(models.Model):
    price = models.FloatField()
    vehicle = models.OneToOneField(Vehicle, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.price) + '$'


class CarModel(models.Model):
    model_name = models.CharField(max_length=100, )
    model_year = models.DateField()
    body_type = models.CharField(max_length=100, )
    image = models.TextField()
    rent_amount = models.IntegerField(default=0)
    vehicle = models.OneToOneField(Vehicle, null=True, on_delete=models.SET_NULL, related_name='vehicle_car')
    car_company = models.ForeignKey(CarCompany, null=True, on_delete=models.SET_NULL, related_name='vehicle_car')

    def __str__(self):
        return str(self.model_name)


class Customer(models.Model):
    sex = {
        ('Male', 'Male'),
        ('Female', 'Female'),
    }
    full_name = models.CharField(max_length=100)
    dob = models.DateField()
    gender = models.CharField(max_length=100, choices=sex)
    passport = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    insurance = models.CharField(max_length=100)
    licence = models.CharField(max_length=100)
    address = models.CharField(max_length=100)

    def __str__(self):
        return str(self.full_name)


class Fine(models.Model):
    fine_cases = models.CharField(max_length=100)
    fine_amount = models.CharField(max_length=100)

    def __str__(self):
        return str(self.fine_cases)


class CarOption(models.Model):
    car_color = (
        ('White', 'White'),
        ('Black', 'Black'),
        ('Gray', 'Gray'),
        ('Red', 'Red'),
        ('Blue', 'Blue'),
    )
    wheel = (
        ('18', '18'),
        ('19', '19')
    )
    material = (
        ('Cloth', 'Cloth'),
        ('Leather', 'Leather'),
    )
    engine = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3')
    )
    car_model = models.ForeignKey(CarModel, null=True, on_delete=models.SET_NULL)
    power = models.CharField(max_length=100, help_text='km/h')
    battery_capacity = models.CharField(max_length=100, help_text='KW')
    color = models.CharField(max_length=100, choices=car_color)
    interior_material = models.CharField(max_length=100, choices=material)
    size_of_wheel = models.CharField(max_length=100, choices=wheel)
    number_of_engine = models.CharField(max_length=100, choices=engine)

    def __str__(self):
        return 'Model: ' + str(self.car_model) + ' Range: ' + str(self.power) + ' Engine: ' + str(self.number_of_engine)


class PaymentMethod(models.Model):
    method = (
        ('Visa', 'Visa'),
        ('Mastercard', 'Mastercard'),
        ('PayPal', 'PayPal'),
    )
    customer = models.OneToOneField(Customer, null=True, on_delete=models.SET_NULL)
    car = models.ForeignKey(CarOption, null=True, on_delete=models.SET_NULL)
    payment_type = models.CharField(max_length=100, choices=method)
    amount = models.FloatField()
    card_number = models.CharField(max_length=100, null=True)
    cvv = models.CharField(max_length=10, null=True)
    start_day = models.DateTimeField(null=True)
    end_day = models.DateTimeField(null=True)
    total_day = models.CharField(max_length=10, null=True)

    def __str__(self):
        return str(self.customer)


class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    text = models.TextField()

    def __str__(self):
        return str(self.email)


class Damaged(models.Model):
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    fine = models.ForeignKey(Fine, null=True, on_delete=models.SET_NULL)
    car_option = models.ForeignKey(CarOption, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return str(self.customer)
