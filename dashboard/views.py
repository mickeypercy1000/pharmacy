from django.shortcuts import render

from stocks.models import Stock
from django.db.models import Sum


# Create your views here.
def dashboard(request):
    user = request.user
    cost_price = Stock.objects.aggregate(Sum('cost_price'))['cost_price__sum']
    selling_price = Stock.objects.aggregate(Sum('selling_price'))['selling_price__sum']
    total_stock = Stock.objects.all()
    sum_indivual_total = Stock.objects.count()
    print("hiiiii", cost_price, selling_price, sum_indivual_total)
    context = {
        'user':user,
        'cost_price': cost_price,
        'selling_price': selling_price,
        'sum_indivual_total': sum_indivual_total,
        }
    return render(request, 'home.html', context)


def sales(request):
    print("hiiiii")
    return render(request, 'sales.html')

