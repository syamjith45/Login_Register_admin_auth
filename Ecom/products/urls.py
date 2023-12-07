from django.urls import path
from .import views
from django.conf import settings

from django.conf.urls.static import static
urlpatterns = [
    path('product/',views.product_list, name='product'),
    path('add_product/',views.add_product, name='add_product')
]

urlpatterns = urlpatterns + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)