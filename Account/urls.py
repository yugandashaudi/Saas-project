from django.urls import path
from .views import userregistrationView,UserLoginView,ViewAllUserinsideGroup,AddGroupAdminUser,UserChangePasswordView,AddAdminUser,addemployeeuser,AddGroupAdmin,AddallAdminuser,GetEmployeeuser,RequestGroupUser

urlpatterns=[
    path('register/',userregistrationView.as_view(),name='register'),
    path('login/',UserLoginView.as_view(),name='login'),
    path('changepassword/',UserChangePasswordView.as_view(),name='changepassword'),
    path('adminwholeuser/',AddallAdminuser.as_view(),name='AddallAdminuser'),
    path('adminparticularuser/<int:id>/',AddAdminUser.as_view(),name='adminuser'),
    path('createusergroup/',AddGroupAdminUser.as_view(),name='createusergroup'),
    path('userinsidegroup/',ViewAllUserinsideGroup.as_view(),name='userinsidegroup'),
    path('employeetargetuser/<int:id>/',GetEmployeeuser.as_view(),name='employeetargetuser'),
    path('employeeuser/',addemployeeuser.as_view(),name='employeeuser'),
    path('admingroup/',AddGroupAdmin.as_view(),name='admingroup'),
    
   
   
    path('requestuser/',RequestGroupUser.as_view(),name='requestuser')
]