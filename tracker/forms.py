from django import forms
from .models import Expense


# forms → Django forms module
# ModelForm → a class that automatically builds a form from a database model
class ExpenseForm(forms.ModelForm): # This class line is mainly for inheriting from the .ModelForm class.

    # Meta → settings for how it behaves, basically the configuration for how it behaves.
    class Meta:

        model = Expense

        # if you want to give all fields, give fields = '__all__'
        fields = ['amount', 'description', 'date', 'category']

        # Widgets are the HTML manipulators. They help to change the look of the html
        # components right from here, that is, with python itself.
        widgets = {

            'date': forms.DateInput(attrs={'type': 'date'})

        }

        