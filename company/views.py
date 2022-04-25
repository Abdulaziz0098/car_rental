from django.contrib import messages
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect
from django.utils.datetime_safe import datetime

from company.forms import *
from company.models import *


def index_page(request):
    company = request.GET.get('company')
    model = request.GET.get('model')
    engine = request.GET.get('engine')
    company_ = []
    model_ = []
    engine_ = []
    for i in CarOption.objects.all():
        if i.number_of_engine not in engine_:
            engine_.append(i.number_of_engine)
        if i.car_model.car_company.company_name not in company_:
            company_.append(i.car_model.car_company.company_name)
        if i.car_model.model_name not in model_:
            model_.append(i.car_model.model_name)
    company_.sort()
    model_.sort()
    engine_.sort()
    try:
        vehicle = CarOption.objects.all().order_by('car_model__rent_amount')[:6]
        if model != '' and engine != '' and company != '':
            result = CarOption.objects.filter(number_of_engine=engine, car_model__model_name=model,
                                              car_model__car_company__company_name=company)
        elif model != '' and engine != '' and company == '':
            result = CarOption.objects.filter(number_of_engine=engine, car_model__model_name=model)
        elif company != '' and engine != '' and model == '':
            result = CarOption.objects.filter(number_of_engine=engine, car_model__car_company__company_name=company)
        else:
            result = CarOption.objects.filter(car_model__model_name=model, car_model__car_company__company_name=company)
        context = {
            'result': result,
            'vehicle': vehicle,
            'company_': company_,
            'model_': model_,
            'engine_': engine_
        }
    except CarOption.DoesNotExist:
        messages.error(request, 'You entered Wrong criteria')
        vehicle = CarOption.objects.all().order_by('car_model__rent_amount')[:6]
        context = {
            'vehicle': vehicle,
        }
    return render(request, 'index.html', context)


def brand_page(request):
    company = Company.objects.all()
    context = {
        'company': company
    }
    return render(request, 'others/brand.html', context)


def contact_page(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'successfully created you can take it from our inventory')
            return redirect('index')
        else:
            messages.error(request, 'wrong attributes entered try again')
            print(form.errors.as_data)
    else:
        form = ContactForm()
    context = {
        'form': form
    }
    return render(request, 'others/contact.html', context)


def fine_page(request):
    fine = Fine.objects.all()
    context = {
        'fine': fine
    }
    return render(request, 'others/fine.html', context)


def listing_page(request):
    vehicle = CarOption.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(vehicle, 6)
    try:
        cars = paginator.page(page)
    except PageNotAnInteger:
        cars = paginator.page(1)
    except EmptyPage:
        cars = paginator.page(paginator.num_pages)

    context = {
        'cars': cars
    }
    return render(request, 'others/listing.html', context)


def payment_page(request, pk):
    vehicle = CarOption.objects.get(id=pk)
    model = vehicle.car_model.model_name
    inventory = vehicle.car_model.vehicle.inventory.location
    print(model)
    if request.method == 'POST':
        start = request.POST.get('start_day')
        end = request.POST.get('end_day')
        date = (datetime.strptime(end, '%Y-%m-%d') - datetime.strptime(start, '%Y-%m-%d')).days
        customer = CustomerForm(request.POST)
        payment = PaymentMethodForm(request.POST)
        if customer.is_valid():
            parent = customer.save()
            parent.save()
            if payment.is_valid():
                child = payment.save(commit=False)
                child.customer = parent
                child.car = vehicle
                child.total_day = date
                child.save()
                CarModel.objects.filter(model_name=model).update(rent_amount=F('rent_amount') + 1)
                messages.success(request, 'successfully created you can take it from ' + inventory)
                return redirect('index')
            else:
                messages.error(request, 'wrong attributes entered try again')
                parent.delete()
                print(payment.errors.as_data)
        else:
            messages.error(request, 'wrong attributes entered try again')
            print(customer.errors.as_data)
    else:
        customer = CustomerForm()
        payment = PaymentMethodForm()

    context = {
        'vehicle': vehicle,
        'customer': customer,
        'payment': payment,
    }
    return render(request, 'others/payment.html', context)


def supply_page(request):
    dealer = CarCompany.objects.all()
    context = {
        'dealer': dealer
    }
    return render(request, 'others/supply.html', context)
