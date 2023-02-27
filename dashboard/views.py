from django.shortcuts import render

# Create your views here.
def dashboard(request):
    user = request.user
    context = {'user':user}
    return render(request, 'home.html', context)



def sales(request):
    print("hiiiii")
    return render(request, 'sales.html')

