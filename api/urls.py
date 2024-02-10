from django.urls import path

from api.views import DonationDetail, DonationList, ProjectDetail, ProjectList, UserDetail, UserList

urlpatterns = [
    path('users/', UserList.as_view()),
    path('users/<int:pk>/', UserDetail.as_view()),

    path('project/', ProjectList.as_view()),
    path('project/<int:pk>/', ProjectDetail.as_view()),

    path('donation/', DonationList.as_view()),
    path('donation/<int:pk>/', DonationDetail.as_view()),

    
]