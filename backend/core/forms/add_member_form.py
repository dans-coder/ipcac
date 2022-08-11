from django import forms
from core.models.person import Person


# creating a form
class PersonForm(forms.ModelForm):
    # create meta class
    class Meta:
        # specify model to be used
        model = Person

        # specify fields to be used
        fields = [
            "alt_name",
            "phone",
            "sex"
        ]

