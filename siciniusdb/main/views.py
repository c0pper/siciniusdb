from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Person
from .forms import CreateNewPerson

# Create your views here.


def home(response):
    people = Person.objects.all()
    return render(response, "main/home.html", {"people": people})


def create(response):
    if response.method == "POST":
        form = CreateNewPerson(response.POST)

        if form.is_valid():
            fname = form.cleaned_data["fname"]
            p = Person(fname=fname)
            p.save()

        return HttpResponseRedirect("main/home.html")
    else:
        form = CreateNewPerson()
    return render(response, "main/create.html", {"form": form})
