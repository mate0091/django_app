"""django_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from sakila import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("act", views.act),
    path("show", views.show_actor),
    path("edit/<int:id>", views.edit_actor),
    path("update/<int:id>", views.update_actor),
    path("delete/<int:id>", views.destroy_actor),

    path("flm", views.flm),
    path("film_show", views.show_film),
    path("film_edit/<int:id>", views.edit_film),
    path("film_update/<int:id>", views.update_film),
    path("film_delete/<int:id>", views.destroy_film),

]
