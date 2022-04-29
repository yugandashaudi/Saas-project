from django.urls import path
from .views import userregistrationView,UserLoginView,UserChangePasswordView

urlpatterns=[
    path('register/',userregistrationView.as_view(),name='register'),
    path('login/',UserLoginView.as_view(),name='login'),
    path('changepassword/',UserChangePasswordView.as_view(),name='changepassword')
]