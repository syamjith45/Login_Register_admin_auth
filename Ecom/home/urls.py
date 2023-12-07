
from django.urls import path
from django.conf import settings

from django.conf.urls.static import static

from .import views
urlpatterns = [
    path('index/',views.get_product, name='index'),
    
]


urlpatterns = urlpatterns + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)