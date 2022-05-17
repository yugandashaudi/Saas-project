from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.views.decorators.csrf import csrf_exempt

from .import views

urlpatterns = [
    path('', views.CreateTenant.as_view(), name='createtenant'),
    path('domain/', csrf_exempt(views.CreateDomain.as_view()),
         name='createdomian'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
