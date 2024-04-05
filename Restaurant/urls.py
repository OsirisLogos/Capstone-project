from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('api/menu-items/', views.MenuItemsView.as_view(), name='menu_list'),
    path('api/menu-items/<int:pk>', views.SingleMenuItemView.as_view(), name='menu_detail'),
]
