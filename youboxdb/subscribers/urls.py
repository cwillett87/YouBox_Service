from django.urls import path
from . import views

urlpatterns = [
    path('user/', views.UserList.as_view()),
    path('user/<str:username>/', views.UserDetail.as_view()),
    path('upgrade/', views.UtokenList.as_view()),
    path('upgrade/<int:user_Id>/', views.UtokenFilter.as_view()),
    path('delete/<int:pk>/', views.UtokenDetail.as_view()),
    path('clothes/', views.ClothingList.as_view()),
    path('clothes/<int:pk>/', views.ClothingDetail.as_view()),
    path('sub/', views.SubscriptionList.as_view()),
    path('sub/<int:pk>/', views.SubscriptionDetail.as_view()),
    path('order/', views.OrderList.as_view()),
    path('order/<int:pk>/', views.OrderDetail.as_view()),
    path('order-filter/<int:user_Id>/', views.OrderFilter.as_view()),
    path('image/', views.ImageList.as_view()),
    path('image-del/<int:pk>/', views.ImageDetail.as_view()),
    path('image-filter-item/<int:item_Id>/', views.ImageFilterItem.as_view()),
    path('image-filter-user/<int:user_Id>/', views.ImageFilterUser.as_view()),
]