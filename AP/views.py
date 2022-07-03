from django.shortcuts import render

from .models import User

# Create your views here.
def show(request):
    person = User.objects.order_by('first_Name')
    context = {'person': person}
    return render(request, 'info.html', context)