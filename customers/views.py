from django.shortcuts import render

# Create your views here.

def ListCustomers(request):
    customers = customers.objects.all()
    
    context = {
        "customers": customers
    }
    return render(request, "customers.html")