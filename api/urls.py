from django.urls import path

from api.views import DonationDetail, DonationList, ProjectDetail, ProjectList, UserList, UserLogin, UserRegister

urlpatterns = [
    
    path('register/',UserRegister.as_view(),name='user_register'),
    path('login/', UserLogin.as_view(), name='user_login'),
    path('register/<int:pk>/', UserList.as_view()),


    path('project/', ProjectList.as_view()),
    path('project/<int:pk>/', ProjectDetail.as_view()),

    path('donation/', DonationList.as_view()),
    path('donation/<int:pk>/', DonationDetail.as_view()),

    
]