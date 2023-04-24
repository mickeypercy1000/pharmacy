from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from .models import Customer


class SubjectCreateView(CreateView):
    model = Customer
    fields = ["name"] # whenever you use a class based view, put the "fields" in a list like i've done


class SubjectListView(ListView):
    model = Customer


def SubjectView(request): 

    newSubject = SubjectCreateView.as_view()(request) # since the two other views are class-based, before you can access them you have to add .as_view() to the view. That is how you access the view.
    subjects = SubjectListView.as_view()(request) # since the two other views are class-based, before you can access them you have to add .as_view() to the view. That is how you access the view.
    context = {}
    context.update(newSubject.context_data) # now you can have access to the request and context_data
    context.update(subjects.context_data)

    return render(request, "cust.html", context=context)

    # Assuming this view was a class-based view, you can access it in your url like this: path('url-name/', SubjectView.as_view(), name='url-name')
