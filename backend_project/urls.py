from django.urls import path, include
from backend_project import views

from django.contrib import admin
from backend_project import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('test/', views.test_key, name='test_key'),
    path('currencies/', views.get_cryptocurrencies, name='get_cryptocurrencies'),
    path('currencies/<int:currency_id>/', views.get_cryptocurrency, name='get_cryptocurrency'),
    path('admin/', admin.site.urls),
    path('api/', include('cryptocurrency.urls')), 
    path('', views.home, name='home'),        
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

