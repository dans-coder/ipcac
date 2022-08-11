from django.urls import path
from .views import (
    PersonListView, add_person
)

app_name = 'core'

urlpatterns = [
    path('', PersonListView.as_view(), name='home'),
    path('add', add_person, name='add'),
]