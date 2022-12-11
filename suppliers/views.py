from django.shortcuts import render

from suppliers.models import Supplier

# Create your views here.
def supplierList(request):
    suppliers = Supplier.objects.all()
    context = {'suppliers': suppliers}
    return render(request, 'stock.html', context)
