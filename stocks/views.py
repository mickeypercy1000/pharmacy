from django.shortcuts import redirect, render
from django.db.models import Q
from stocks.models import DrugClass, Stock
from suppliers.models import Supplier
from django.contrib import messages

# Create your views here.
def supplierList(request):
    suppliers = Supplier.objects.all()
    context = {'suppliers': suppliers}
    return render(request, 'stock.html', context)


def stock(request):
    stock = Stock.objects.all()
    all_drug_class = DrugClass.objects.all()
    suppliers = Supplier.objects.all()

    if request.method == 'POST' and request.POST.get('add_supplier') is None:
        new_item_class = request.POST.get('new_item_class')
        if new_item_class is not None:
            check_uniqueness = DrugClass.objects.filter(name=new_item_class).first()
            if check_uniqueness is None:
                drug_class = DrugClass.objects.create(name=new_item_class, created_by=request.user)
                drug_class.save()
            # else:
            #     messages.error(request, "This item already exists")

    elif request.method == 'POST' and request.POST.get('new_item_class') is None and request.POST.get('add_supplier'):
        item_name = request.POST.get('item_name')
        item_class = request.POST.get('item_class')
        maximum_quantity = request.POST.get('maximum_quantity')
        reorder_quantity = request.POST.get('reorder_quantity')
        shelf_number = request.POST.get('shelf_number')
        expiry_date = request.POST.get('expiry_date')
        status = request.POST.get('status')
        print('name', item_name)
        print('item_class', item_class)
        print('maximum_quantity', maximum_quantity)
        print('reorder_quantity', reorder_quantity)
        print('shelf_number', shelf_number)
        print('status', status)

        stock = Stock.objects.create(
            name=item_name,
            # item_class = selected_drug_class,
            maximum_quantity=maximum_quantity,
            reorder_quantity=reorder_quantity,
            shelf_number=shelf_number,
            expiry_date=expiry_date,
            status=status,
            deleted=False,
            created_by=request.user
            )

        stock.save()
        return redirect('stock')

    context = {
        'stock': stock,
        'suppliers': suppliers,
        'all_drug_class': all_drug_class,
        
        }
    return render(request, 'stock.html', context)


def addItemClass(request):
    if request.method == 'POST':
        new_item_class = request.POST.get('new_item_class')
        print('item', new_item_class)
        drug_class = DrugClass.objects.create(name=new_item_class)
        drug_class.save()
        return redirect('stock')
    return render(request, 'stock.html')


def deleteStock(request, id):
    if request.method == 'POST':
        stock = Stock.objects.filter(id = id).first()
        if stock is not None:
            stock.delete()
        return redirect('stock')
    return render(request, 'stock.html')


def expiry(request):
    # expiry_date_setup = request.POST.get('expiry_date_setup')
    # if expiry_date_setup is not None:
    #     expiry = Stock.objects.filter(expiry_date__lte = expiry_date_setup)
    #     context = {'expiry': expiry}
    return render(request, 'expiry.html')
        


