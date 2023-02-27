import re
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from suppliers.apps import SuppliersConfig
from suppliers.models import Supplier


# Create your views here.

def suppliers(request):

    # all_suppliers = Supplier.objects.all()
    # if request.method == 'POST':
    all_suppliers = ""

    if (
        request.method == 'POST'
        and request.POST.get('supplier_name') is not None
        and request.POST.get('supplier_address') is not None
        and request.POST.get('supplier_phone') is not None
    ):
        supplier_name = request.POST.get('supplier_name')
        supplier_address = request.POST.get('supplier_address')
        supplier_phone = request.POST.get('supplier_phone')

        if supplier_name is not None and supplier_address is not None and supplier_phone is not None:
            check_uniqueness = Supplier.objects.filter(name=supplier_name).first()
            if check_uniqueness is None:
                supplier = Supplier.objects.create(name=supplier_name, address=supplier_address, phone=supplier_phone, created_by=request.user)
                supplier.save()
                messages.success(request, f"{supplier_name} successfully added")
                return redirect('suppliers')
            else:
                messages.error(request, f"{supplier_name} already exists")

    elif request.method == 'POST' and request.POST.get('fromDate') is not None and request.POST.get('toDate') is not None:
        # fromdate = request.POST['fromDate']
        fromdate = request.POST.get('fromDate')
        todate = request.POST.get('toDate')
        print("ddddd", fromdate)
        stringified_fromdate = fromdate + ' '+'00:00:00'
        stringified_todate = todate + ' '+'23:59:59'
        # todate = request.POST['toDate']

        if stringified_fromdate and stringified_todate:
            supplier_filter = Supplier.objects.filter(created_at__gte=stringified_fromdate, created_at__lte=stringified_todate)
            if supplier_filter:
                all_suppliers = supplier_filter

    else:
        all_suppliers = Supplier.objects.all()

    context = {
        'all_suppliers': all_suppliers
    }
    return render(request, 'suppliers.html', context)


def updateSupplier(request, supplier_id):

    supplier = get_object_or_404(Supplier, id=supplier_id)
    if request.method == 'POST':
        supplier_name = request.POST.get('supplier_name')
        supplier_address = request.POST.get('supplier_address')
        supplier_phone = request.POST.get('supplier_phone')

        if supplier_name is not None and supplier_address is not None and supplier_phone is not None:
            Supplier.objects.filter(id=supplier_id).update(
                name=supplier_name,
                address=supplier_address,
                phone=supplier_phone
            )
        return redirect('suppliers')

    context = {'supplier': supplier}
    return render(request, 'updateSupplier.html', context)


def deleteSupplier(request, supplier_id):
    print('deleteSupplier')
    supplier = Supplier.objects.filter(id=supplier_id).first()

    if request.method == 'POST': 
        supplier.delete()
        return redirect('suppliers')
    return render(request, 'deleteSupplier.html')


def dateFilter(request):
    if request.method == 'POST':
        fromdate = request.POST['fromdate']+' '+'00:00:00'
        todate = request.POST['todate']+' '+'23:59:59'
        suppliers = Supplier.objects.filter(created_at__gte=fromdate, created_at__lte=todate)
        print('date', fromdate, todate, suppliers)

        return redirect('suppliers')
    context = {'suppliers': suppliers}
    return render(request, 'suppliers.html', context)
