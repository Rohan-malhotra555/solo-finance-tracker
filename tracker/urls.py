from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

# BEST PRACTICE: always place a trailing / at the end of the url.

urlpatterns = [
    # this means that there is no path in the app urls.py file, so if 
    # main urls.py file also has "", then website.com directly calls the dashboard func.
    # '' means everything.
    path('', views.dashboard, name="dashboard"), # READ url of CRUD
    path('add/', views.add_expense, name="add_expense"), # CREATE url of CRUD
    path('edit/<int:expense_id>/', views.edit_expense, name="edit_expense"), # UPDATE url of CRUD
    path('delete/<int:expense_id>/', views.delete_expense, name="delete_expense"), # DELETE url of CRUD

    # Login and logout urls.
    # auth_views is the alias for views which is the Class Based View (CBV) given by
    # django. It has the authentication views already written for login and logout.
    # We use .as_view because the urls require a function to handover the processing. 
    # So, it essentially converts the CBV to FBV. Everything, be it forms, logic, views etc.
    # everything is provided by Login and Logout views.
    path('login/', auth_views.LoginView.as_view(template_name="tracker/login.html"), name="login"),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),

    path('register/', views.register, name="register"),

    path('profile/edit/', views.edit_profile, name="edit_profile"),
    
]
