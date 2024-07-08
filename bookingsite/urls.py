from django.urls import path
from . import views
from .views import CustomLoginView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('nav/', views.NavigationView.as_view(), name='nav'),
    path('', views.EntryView.as_view(), name = 'home')
    # path('book/', views.book, name='book'),
]