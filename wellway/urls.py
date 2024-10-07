"""
URL configuration for wellway project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from pages.views import main, Route_1, Route_2, Route_3, Route_4, Route_5, add_review
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main, name='MainPage'),
    path('Route1/', Route_1, name='Route_1'),
    path('Route2/', Route_2, name='Route_2'),
    path('Route3/', Route_3, name='Route_3'),
    path('Route4/', Route_4, name='Route_4'),
    path('Route5/', Route_5, name='Route_5'),
    path('users/', include('users.urls', namespace='users')),
    path('AddReview/', add_review, name='Add_Review'),

]

if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)