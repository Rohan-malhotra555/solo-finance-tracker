"""
URL configuration for finance_tracker project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # include tells: If the URL matches this prefix, hand over control to another file (app’s urls.py)
    # '' means everything
    path('', include('tracker.urls'))
]


# If we are developing locally on our machine (DEBUG = True)
if settings.DEBUG:

    # Tell the switchboard to route MEDIA_URL requests to the physical MEDIA_ROOT folder
    # Literally tells, if the url begins with media url that is '/media/',
    # then go to the MEDIA_ROOT, GRAB THE FILE AND SERVE IT.
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)