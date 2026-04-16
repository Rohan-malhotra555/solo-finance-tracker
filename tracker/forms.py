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

            'amount': forms.NumberInput(attrs={'class': 'w-full p-2 border border-gray-300 rounded mt-1 focus:ring-orange-500 focus:border-orange-500'}),
            'description': forms.TextInput(attrs={'class': 'w-full p-2 border border-gray-300 rounded mt-1 focus:ring-orange-500 focus:border-orange-500'}),
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'w-full p-2 border border-gray-300 rounded mt-1 focus:ring-orange-500 focus:border-orange-500'}),
            'category': forms.Select(attrs={'class': 'w-full p-2 border border-gray-300 rounded mt-1 focus:ring-orange-500 focus:border-orange-500'}),

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


    # we are doing this because here, in this form, we don't have fields in our hand.
    # This runs the moment the form is created
    def __init__(self, *args, **kwargs):
        # Let Django do its normal setup first, that is, let it create the fields first.
        super().__init__(*args, **kwargs)
        
        # Now, loop through EVERY field in the form and attach Tailwind classes!
        # self.field.items() creates a tuple formation like this:
        # (username, <charfield>),
        # (password. <passwordfield>)

        # so that is why we are storing field_name and field.
        # then each field, that is, say <charfield> has widgets, and we are updating it's attribute dict.
        for field_name, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'w-full p-2 border border-gray-300 rounded mt-1 focus:ring-orange-500 focus:border-orange-500'
            })




# Form to update/edit the user profile.
class ProfileUpdateForm(forms.ModelForm):

    class Meta:

        model = get_user_model()

        fields = ['username', 'first_name', 'last_name', 'bio', 'profile_picture']


        # adding these as form.as_p displays the fields by itself.
        # we can also do the __init__ method though, then in the html template, we use 
        # for field in form:
        widgets = {
            'username': forms.TextInput(attrs={'class': 'w-full p-2 border border-gray-300 rounded mt-1 focus:ring-orange-500 focus:border-orange-500'}),
            'first_name': forms.TextInput(attrs={'class': 'w-full p-2 border border-gray-300 rounded mt-1 focus:ring-orange-500 focus:border-orange-500'}),
            'last_name': forms.TextInput(attrs={'class': 'w-full p-2 border border-gray-300 rounded mt-1 focus:ring-orange-500 focus:border-orange-500'}),
            
            # Textarea allows us to specify 'rows' to make the box taller
            'bio': forms.Textarea(attrs={'class': 'w-full p-2 border border-gray-300 rounded mt-1 focus:ring-orange-500 focus:border-orange-500', 'rows': 4}),
            
            # FileInput gives us the standard "Choose File" button
            'profile_picture': forms.FileInput(attrs={'class': 'w-full p-2 border border-gray-300 rounded mt-1 bg-white focus:ring-orange-500 focus:border-orange-500'}),
        }

