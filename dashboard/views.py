from django.shortcuts import render

from stock.models import Stock
from django.db.models import Sum


# Create your views here.
def dashboard(request):
    user = request.user
    # total_stock = Stock.sum_quantity()
    # print(total_stock)

    cost_price = Stock.objects.aggregate(Sum('cost_price')).get('cost_price__sum', 0)
    if not cost_price:
        cost_price = 0.00

    selling_price = Stock.objects.aggregate(Sum('selling_price'))['selling_price__sum']
    if not selling_price:
        selling_price = 0.00

    total_stock = Stock.objects.aggregate(Sum('quantity'))['quantity__sum']
    if not total_stock:
        total_stock = 0

    sum_indivual_total = Stock.objects.count()
    print("hiiiii", cost_price, selling_price, sum_indivual_total)
    context = {
        'user':user,
        'cost_price': cost_price,
        'selling_price': selling_price,
        'sum_indivual_total': sum_indivual_total,
        'total_stock': total_stock,
        }
    return render(request, 'home.html', context)

