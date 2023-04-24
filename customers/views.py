from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from customers.models import Customer


# Create your views here.
def customers(request):

    all_customers = ""

    if (
        request.method == 'POST'
        and request.POST.get('customer_name') is not None
        and request.POST.get('customer_address') is not None
        and request.POST.get('customer_phone') is not None
        and request.POST.get('id_card_number') is not None
    ):
        customer_name = request.POST.get('customer_name')
        customer_address = request.POST.get('customer_address')
        customer_phone = request.POST.get('customer_phone')
        id_card_number = request.POST.get('id_card_number')

        if customer_name is not None and customer_address is not None and customer_phone is not None and id_card_number is not None:
            check_uniqueness = Customer.objects.filter(id_card_number=id_card_number).first()
            if check_uniqueness is None:
                customer = Customer.objects.create(
                    name=customer_name,
                    address=customer_address,
                    phone=customer_phone,
                    id_card_number=id_card_number,
                    created_by=request.user
                )
                print("the customer", customer)
                customer.save()
                messages.success(request, f"{customer_name} successfully added")
                return redirect('customers')
            else:
                messages.error(request, f"{customer_name} already exists")

    elif request.method == 'POST' and request.POST.get('fromDate') is not None and request.POST.get('toDate') is not None:
        # fromdate = request.POST['fromDate']
        fromdate = request.POST.get('fromDate')
        todate = request.POST.get('toDate')
        print("ddddd", fromdate)
        stringified_fromdate = fromdate + ' '+'00:00:00'
        stringified_todate = todate + ' '+'23:59:59'
        # todate = request.POST['toDate']

        if stringified_fromdate and stringified_todate:
            customer_filter = Customer.objects.filter(created_at__gte=stringified_fromdate, created_at__lte=stringified_todate)
            if customer_filter:
                all_customers = customer_filter

    else:
        all_customers = Customer.objects.all()

    context = {
        'all_customers': all_customers
    }
    return render(request, 'customers.html', context)


def updateCustomer(request, customer_id):

    print("hiiiiiiii")
    customer = get_object_or_404(Customer, id=customer_id)
    if request.method == 'POST':
        customer_name = request.POST.get('customer_name')
        customer_address = request.POST.get('customer_address')
        customer_phone = request.POST.get('customer_phone')
        id_card_number = request.POST.get('id_card_number')
        if customer_name is not None and customer_address is not None and customer_phone is not None and id_card_number is not None:
            Customer.objects.filter(id=customer_id).update(
                name=customer_name,
                address=customer_address,
                phone=customer_phone,
                id_card_number=id_card_number,
            )
        return redirect('customers')

    context = {'customer': customer}

    return render(request, 'updateCustomer.html', context)


def deleteCustomer(request, customer_id):
    print('deleteCustomer')
    customer = Customer.objects.filter(id=customer_id).first()

    if request.method == 'POST': 
        customer.delete()
        return redirect('customers')
    return render(request, 'deleteCustomer.html')

