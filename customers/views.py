from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from customers.models import Customer


# Create your views here.
def customers(request):
    print('hhhhhhhh')
    all_customers = Customer.objects.all()

    customer_name = request.POST.get('customer_name')
    customer_address = request.POST.get('customer_address')
    customer_phone = request.POST.get('customer_phone')
    id_card_number = request.POST.get('id_card_number')
    if customer_name is not None and customer_address is not None and customer_phone is not None and id_card_number is not None:
        print('all done')
        
        check_uniqueness = Customer.objects.filter(id_card_number=id_card_number).first()
        if check_uniqueness is not None:
            messages.error(request, "This customer already exists")

        else:
            customer = Customer.objects.create(
                name=customer_name,
                address=customer_address,
                phone=customer_phone,
                id_card_number=id_card_number,
                created_by=request.user
                )
            customer.save()
            messages.success(request, f"{customer_name} successfully added")
            return redirect('customers')

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

