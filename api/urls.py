from django.urls import path

from api.views import DonationDetail, DonationList, ProjectDetail, ProjectList, UserDetail, UserList

urlpatterns = [
    path('Users/', UserList.as_view()),
    path('Users/<int:pk>/', UserDetail.as_view()),

    path('Project/', ProjectList.as_view()),
    path('Project/<int:pk>/', ProjectDetail.as_view()),

    path('Donation/', DonationList.as_view()),
    path('Donation/<int:pk>/', DonationDetail.as_view()),

    
]