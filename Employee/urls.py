from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns =[
    path('',views.home,name='home'),
    path('adminorder/',views.adminorder,name='adminorder'),
    path('userorder/',views.userorder,name='userorder'),
    path('groupwork/',views.groupwork,name='groupwork'),
    path('userwork/',views.userwork,name='userwork'),
    path('allgroupwwork/',views.allgroupwork,name='allgroupwork'),
    path('alluserwwork/',views.alluserwork,name='alluserwork'),
    path('update_userwork/<int:id>/',views.update_userwork,name='update_userwork'),
    path('my_group_works/',views.my_group_works,name='my_group_works')
    
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)