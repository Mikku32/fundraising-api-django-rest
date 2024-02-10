from django.urls import path

from api.views import UserList

urlpatterns = [
    path('Users/', UserList.as_view()),
]