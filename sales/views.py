from django.shortcuts import render

from sales.models import Sales
from stock.models import Stock


# Create your views here.
def allSales(request):
    all_filtered_stock = Stock.objects.all()
    sales = Sales.objects.all()
    context = {
        "sales": sales,
        'all_filtered_stock': all_filtered_stock
        }
    return render(request, 'sales.html', context)

