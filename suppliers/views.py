import re
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from suppliers.models import Supplier


# Create your views here.

def suppliers(request):

    all_suppliers = Supplier.objects.all()

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