from django.shortcuts import render, HttpResponse
from datetime import datetime
from Myapp.models import Contact
from django.contrib import messages


# Create your views here.
def index(request):
    context = {
    }
    return render(request, "index.html", context)
    # return HttpResponse("This is home page.")


def about(request):
    return render(request, "about.html")
    # return HttpResponse("This is about page.")


def services(request):
    return render(request, "services.html")
    # return HttpResponse("This is services page.")


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        desc = request.POST.get('desc')
        contact1 = Contact(name=name, email=email, password=password, desc=desc, date=datetime.today())
        contact1.save()
        messages.success(request, 'Congrats! Your form is submitted.')
    return render(request, "contact.html")
    # return HttpResponse("This is contact page.")
