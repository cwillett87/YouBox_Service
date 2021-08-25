from django.urls import path
from .views import *
from django.conf.urls import url

from rest_framework.authtoken.views import obtain_auth_token



urlpatterns = [
    path('user/', UserList.as_view()),
    path('user/<str:username>/', UserDetail.as_view()),
    path('upgrade/', UtokenList.as_view()),
    path('upgrade/<int:user_Id>/', UtokenFilter.as_view()),
    path('delete/<int:pk>/', UtokenDetail.as_view()),
    path('clothes/', ClothingList.as_view()),
    path('clothes/<int:pk>/', ClothingDetail.as_view()),
    path('clothes-filter/<str:style>/', ClothingFilter.as_view()),
    path('sub/', SubscriptionList.as_view()),
    path('sub/<int:pk>/', SubscriptionDetail.as_view()),
    path('order/', OrderList.as_view()),
    path('order/<int:pk>/', OrderDetail.as_view()),
    path('order-filter/<int:user_Id>/', OrderFilter.as_view()),
    path('image/', ImageList.as_view()),
    path('image-del/<int:pk>/', ImageDetail.as_view()),
    path('image-filter-item/<int:item_Id>/', ImageFilterItem.as_view()),
    path('image-filter-user/<int:user_Id>/', ImageFilterUser.as_view()),
    path('upload/', ImageList.as_view(), name='upload'),
    path('logout/<str:username>/', Logout.as_view()),
    url(r'^authenticate/', CustomObtainAuthToken.as_view()),
]