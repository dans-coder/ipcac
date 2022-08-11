import django_tables2 as tables
from core.models import Person

class PersonTable(tables.Table):
    class Meta:
        model = Person
        template_name = "django_tables2/bootstrap.html"
        fields = ("alt_name", "phone", "sex")
