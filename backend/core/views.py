from django.contrib import messages
from django.views.generic import ListView
from django.shortcuts import redirect, render
from django.utils import timezone
from .forms.add_member_form import PersonForm
from django_tables2 import SingleTableView
from .models import Person
from .tables.person_table import PersonTable

class PersonListView(SingleTableView):
    model = Person
    table_class = PersonTable
    template_name = 'home.html'


def add_person(request):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization
    form = PersonForm(request.POST or None)
    if form.is_valid():
        form.save()

    context['form'] = form
    return render(request, "add_member.html", context)