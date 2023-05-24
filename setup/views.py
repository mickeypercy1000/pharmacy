from django.shortcuts import render, redirect

from stock.models import ExpiryAlert, ItemClass

# Create your views here.
def expiry_setup(request):
    
    expiry_alert_selected = ExpiryAlert.objects.first()

    if request.method == 'POST' and request.POST.get('expiry_alert') is not None:
        expiry_alert = request.POST.get('expiry_alert')
        alert = ExpiryAlert.objects.create(expiry_alert=expiry_alert, created_by=request.user)
        alert.save()
        return redirect('expiry-setup')
    context = {
        'expiry_alert_selected': expiry_alert_selected
        }
    return render(request, 'setup.html', context)


def item_class_setup(request):
    item_class = None
    
    if request.method == 'POST' and request.POST.get('new_item_class') is not None:
        new_item_class = request.POST.get('new_item_class')
        item_class = ItemClass.objects.create(name=new_item_class, created_by=request.user)
        item_class.save()
        return redirect('expiry-setup')
    context = {
        "item_class": item_class
    }
    return render(request, 'setup.html', context)