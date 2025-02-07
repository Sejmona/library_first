"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from knihovna import views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),  # Hlavní stránka
    path('writers/', views.writers, name='writers'),  # Sekce Spisovatelé
    path('writers/<str:name>/', views.writer_detail, name='writer_detail'),  # Detail spisovatele
    path('writers/<str:name>/<str:book>/', views.writer_book_detail, name='writer_book_detail'),  # Detail knihy od konkrétního autora
    path('knihy/', views.best_books, name='best_books'),  # Sekce Nejlepší knihy
    path('books/<int:position>/', views.book_detail, name='book_detail'),  # Detail knihy podle pořadí
]




