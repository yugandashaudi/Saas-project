from django.urls import path
from .views import userregistrationView

urlpatterns=[
    path('register/',userregistrationView.as_view(),name='register')
]