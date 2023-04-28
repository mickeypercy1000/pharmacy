import datetime
import re
from types import new_class
from django.shortcuts import get_object_or_404, redirect, render
from django.db.models import Q
from stock.models import ExpiryAlert, ItemClass, Stock, StockAdjustment
from suppliers.models import Supplier
from django.contrib import messages


# Create your views here.

def stock(request):

    all_stock = ""
    expiry_alert_selected = ExpiryAlert.objects.first()
    print("selected", expiry_alert_selected)

    # DATE FILTER 
    if request.method == 'POST' and request.POST.get('fromDate') is not None and request.POST.get('toDate') is not None:
        print("its here 33333333")

        fromdate = request.POST.get('fromDate')
        todate = request.POST.get('toDate')
        stringified_fromdate = fromdate + ' '+'00:00:00'
        stringified_todate = todate + ' '+'23:59:59'
        print("qqqqqqqqqqqqqqq", fromdate)
        print("pppppppppkkkkkkkkkk", todate)

        if stringified_fromdate and stringified_todate:
            stock_filter = Stock.objects.filter(created_at__gte=stringified_fromdate, created_at__lte=stringified_todate)
            if stock_filter:
                all_stock = stock_filter  
    else:
        all_stock = Stock.objects.all()
    context = {
        'expiry_alert_selected': expiry_alert_selected,
        'all_stock': all_stock,
        }
    return render(request, 'stock.html', context)


def itemAdjustment(request):
    # if request.method == 'POST':
    all_stock = Stock.objects.all()

    search_item_name = request.POST.get('search_item_name')
    current_quantity = request.POST.get('current_quantity')
    new_quantity = request.POST.get('new_quantity')
    reason_for_adjustment = request.POST.get('reason_for_adjustment')
    filter_search_item = Stock.objects.filter(name=search_item_name).first()
    if filter_search_item is not None:
        adjustment = StockAdjustment.objects.create(
            name=search_item_name,
            current_quantity=current_quantity,
            new_quantity=new_quantity,
            reason_for_adjustment=reason_for_adjustment
            )
        adjustment.save()

        search_item_name.quantity = new_quantity
        search_item_name.save()

        return redirect('stock')
    context = {
        'search_item_name': search_item_name,
        'all_stock': all_stock
    }
    return render(request, 'adjustments.html', context)


def addStock(request):
    all_drug_class = ItemClass.objects.all()
    # print(all_drug_class)


    if request.method == 'POST':
        item_name = request.POST.get('item_name')
        item_class = request.POST.get('select_item_group')
        maximum_quantity = request.POST.get('maximum_quantity')
        reorder_quantity = request.POST.get('reorder_quantity')
        quantity = request.POST.get('item_quantity')
        expiry_date = request.POST.get('expiry_date')
        selling_price = request.POST.get('selling_price')
        cost_price = request.POST.get('cost_price')
        shelf_number = request.POST.get('shelf_number')
        status = request.POST.get('select_item_status')
        print('name', item_name)
        print('item_class', item_class)
        print('maximum_quantity', maximum_quantity)
        print('reorder_quantity', reorder_quantity)
        print('quantity', quantity)
        print('expiry_date', expiry_date)
        print('selling_price', selling_price)
        print('cost_price', cost_price)
        print('shelf_number', shelf_number)
        print('status', status)

        new_item = ItemClass.objects.filter(name=item_class).first()
        print('new_item', new_item)

        stock = Stock.objects.create(
            name=item_name,
            item_class = new_item,
            maximum_quantity=maximum_quantity,
            reorder_quantity=reorder_quantity,
            quantity=quantity,
            expiry_date=expiry_date,
            selling_price=selling_price,
            cost_price=cost_price,
            shelf_number=shelf_number,
            status=status,
            deleted=False,
            created_by=request.user
            )

        stock.save()
        return redirect('add-stock')
    context = {'all_drug_class': all_drug_class}
    return render(request, 'addStock.html', context)


def updateStock(request, stock_id):
    print('here now')
    stock = get_object_or_404(Stock, id=stock_id)
    print("nnnnnmnmnnmnm", stock.name)
    all_drug_class = ItemClass.objects.all().exclude(name=stock.item_class)
    print(stock.expiry_date)
    if request.method == 'POST':
        item_name = request.POST.get('item_name')
        item_class = request.POST.get('select_item_group')
        maximum_quantity = request.POST.get('maximum_quantity')
        reorder_quantity = request.POST.get('reorder_quantity')
        quantity = request.POST.get('item_quantity')
        expiry_date = request.POST.get('expiry_date')
        selling_price = request.POST.get('selling_price')
        cost_price = request.POST.get('cost_price')
        shelf_number = request.POST.get('shelf_number')
        status = request.POST.get('select_item_status')

        new_item = ItemClass.objects.filter(name=item_class).first()
        if (
            item_name is not None and
            item_class is not None and
            maximum_quantity is not None and
            reorder_quantity is not None and
            quantity is not None and
            expiry_date is not None and
            selling_price is not None and
            cost_price is not None and
            shelf_number is not None and 
            status is not None
            ):
            Stock.objects.filter(id=stock_id).update(
                name=item_name,
                item_class = new_item,
                maximum_quantity=maximum_quantity,
                reorder_quantity=reorder_quantity,
                quantity=quantity,
                expiry_date=expiry_date,
                selling_price=selling_price,
                cost_price=cost_price,
                shelf_number=shelf_number,
                status=status,
            )
            return redirect('stock')

    context = {'stock': stock, 'all_drug_class': all_drug_class}

    return render(request, 'updateStock.html', context)

def deleteStock(request, stock_id):
    stock = get_object_or_404(Stock, id=stock_id)
    if stock:
        if request.method == 'POST': 
            stock.delete()
            return redirect('stock')
    return render(request, 'deleteStock.html')