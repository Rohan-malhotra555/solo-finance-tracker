from django import forms
from .models import Expense
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


# forms → Django forms module
# ModelForm → a class that automatically builds a form from a database model
# form to add new expense.
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

# Form for new user registration
class RegisterForm(UserCreationForm):

    # UserCreationForm.Meta: This means, inheriting the Meta class from UCF.
    # This means:
    # You keep all default settings (like fields, validation behavior, etc.)
    # You can override only what you need
    # So basically, WE ARE JUST REPLACING THE USER MODEL, REST EVERYTHING IS SAME.
    class Meta(UserCreationForm.Meta):

        model = get_user_model()
        # We inherit the default fields (username, password 1, password 2)
        fields = UserCreationForm.Meta.fields


# Form to update/edit the user profile.
class ProfileUpdateForm(forms.ModelForm):

    class Meta:

        model = get_user_model()

        fields = ['username', 'first_name', 'last_name', 'bio', 'profile_picture']

