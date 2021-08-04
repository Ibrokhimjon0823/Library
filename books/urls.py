from django.urls import path
from .views import BookListView

urlpattern = [
    path('', BookListView.as_view(), name = 'home')
]