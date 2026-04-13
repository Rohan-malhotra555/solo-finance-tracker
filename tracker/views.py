from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Sum
from .models import Expense, Category
from .forms import ExpenseForm, RegisterForm
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login



# Create your views here.



# ------------------------------------

# START OF CRUD OPERATIONS

# ------------------------------------

# This is the dashboard view. When a user first searches this websites name, e.g.
# finance-tracker.com, the tracker/urls.py file will fetch this view.
# This is the READ part of CRUD

def dashboard(request):

    # order_by('created_at') → 2020, 2022, 2024 (ascending) (oldest first) (small to big)
    # order_by('-created_at') → 2024, 2022, 2020 (descending) (newest first) (big to small)
    all_expenses = Expense.objects.filter(user = request.user).order_by('-date') 


    # START OF FILTERING LOGIC

    categories = Category.objects.filter(created_by = request.user)

    category_filter = request.GET.get('category')

    if category_filter:
        
        # narrowing down the expenses based on the category.
        all_expenses = all_expenses.filter(category__name = category_filter)

    # END OF FILTERING LOGIC

    amount_data = all_expenses.aggregate(total = Sum('amount'))

    # we can also write amount_data['total] or 0, in order to check if the returned value
    # is None. (check once)
    total_amount = amount_data['total']

    # if the amount will be 0, then django doesn't return 0, it returns None.
    # That is why it is required to check if it's 0.
    if total_amount is None:
        total_amount = 0
    
    context = {
        'all_expenses': all_expenses,
        'total_amount': total_amount,
        'categories': categories,
    }

    return render(request, 'tracker/dashboard.html', context)



# This view is used to handle the ExpenseForm and display to the user, the form 
# when they try to add a new expense
# This is the CREATE part of CRUD.
def add_expense(request):

    # Checking if the method is POST in the form.
    if request.method == 'POST':

        # Attaching the data filled by the user to the form.
        form  = ExpenseForm(request.POST)

        # Checks if the form fields are correct as per the norms and db.
        if form.is_valid():

            # We let django create the object(unsave instance) but stop it from committing 
            # to the database, because we need to set the user manually, for security and UX reasons.
            expense = form.save(commit=False)
            expense.user = request.user #gives error this not set here.
            expense.save() # calling the save and finally committing.

        return redirect('dashboard') # using the url name dashboard to redirect the user.
    
    else:
        # displaying a blank form if the user just came to the page and didn't fill anything.
        form = ExpenseForm()
    
    # Only used when form is empty, that is the else part, because POST part will redirect always.
    context = {
        'form': form,
    }

    return render(request, 'tracker/add_expense.html', context)


# This is the UPDATE part of CRUD
def edit_expense(request, expense_id):

    # 1. Fetch the exact expense safely. If a user types a random ID in the URL, throw a 404 Not Found.
    # Security check: we also filter by user=request.user so user A can't edit User B's expense!
    # The user is checked to prevent IDOR vulnerability, where a user can manually change the id in the url and access 
    # unauthorized data. So, basically, first fetching by id and then checking the user.
    target_expense = get_object_or_404(Expense, id=expense_id, user=request.user)

    if request.method == 'POST':

        # 2. The user submitted new edits. We bind the POST data AND the existing object to the form.
        # we give instance again otherwise just request.POST will create a new duplicate object.
        # Thus, django will run an UPDATE command instead of an INSERT command.
        form = ExpenseForm(request.POST, instance=target_expense)

        if form.is_valid():

            # 3. We don't need commit=False here because the user is already attached to this existing expense.
            form.save()

        return redirect('dashboard')

    else:
        # 4. The user just arrived. We pass the existing expense into the form to pre-fill the HTML boxes.
        form = ExpenseForm(instance=target_expense)

    
    context = {
        'form': form,
    }

    return render(request, 'tracker/add_expense.html', context)


# This is the DELETE part of CRUD
def delete_expense(request, expense_id):

    target_expense = get_object_or_404(Expense, id=expense_id, user=request.user)

    # Only if the request's method is POST, we delete the expense object.
    if request.method == 'POST':
        target_expense.delete()
        return redirect('dashboard')
    
    # else, we redirect the user to the confirmation page so that they can click the delete button
    # that acutally makes this request a POST request.
    context = {

        'target_expense': target_expense,

    }

    return render(request, 'tracker/delete_expense.html', context)


# ------------------------------------

# END OF CRUD OPERATIONS

# ------------------------------------



# New user REGISTRATION VIEW

def register(request):

    if request.method == 'POST':

        # We can't directly use this UserCreationForm. Reason being, this built-in
        # form talks and saves only to the default user model. But we are using 
        # our own model. So, we need to make a new form inheriting from this form
        # and then save the new user, which will be saved to our custom user model.
        # form = UserCreationForm(request.POST) (can't be used with custom user.)

        form = RegisterForm(request.POST)

        if form.is_valid():

            user = form.save()

            login(request, user)

            return redirect('dashboard')
    
    else:

        # form = UserCreationForm()

        form = RegisterForm()
    
    context = {
        'form': form,
    }

    return render(request, 'tracker/register.html', context)
        
        
        