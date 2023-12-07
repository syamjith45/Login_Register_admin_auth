from django.urls import path
from .import views
from django.conf import settings  
from django.conf.urls.static import static
urlpatterns = [
    path('login/', views.login_user, name='login'),
    path('home/', views.home, name='home'),
    # path('logout/',views.logout_user,name='logout')
    path('register/',views.register_user,name='register'),
    path('admin_home/', views.admin_home, name='admin_home')
]
urlpatterns = urlpatterns + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)