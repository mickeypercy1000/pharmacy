from django.shortcuts import render

from sales.models import Sales

# Create your views here.
def allSales(request):
    sales = Sales.objects.all()
    context = {"sales": sales}
    return render(request, 'sales.html', context)
