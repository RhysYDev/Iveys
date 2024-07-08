from django.urls import path
from . import views
from .views import CustomLoginView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('', views.NavigationView.as_view(), name='home')
    # path('book/', views.book, name='book'),
]