
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.urls.conf import include
from django.conf import settings
from app_seguridad import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index" ),
    path('login/', views.log_in, name="login_view"),
    path('logout/', views.log_out, name="logout_view"),
    path('transportAgency/', include('app_transportAgency.urls'))

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)



