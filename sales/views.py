from django.shortcuts import render

from sales.models import Sales
from stocks.models import Stock

# Create your views here.
def allSales(request):
    sales = Sales.objects.all()
    context = {"sales": sales}
    return render(request, 'sales.html', context)


def salesDetails(request, id):
    stock = Stock.objects.filter(id=id).first()
    return Response({
        "item_name": stock.name,
        "item_price": stock.price,
        "item_name": stock.name,
        "item_name": stock.name,
    })
