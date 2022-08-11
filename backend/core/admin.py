from core.models.person import Person
from django.contrib import admin

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('id', '__unicode__')