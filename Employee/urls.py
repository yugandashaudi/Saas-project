
from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.decorators.csrf import csrf_exempt
urlpatterns =[
    path('',views.CreateTenant.as_view(),name='createtenant'),
  
    path('domain/',csrf_exempt(views.CreateDomain.as_view()),name='createdomian')
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)

