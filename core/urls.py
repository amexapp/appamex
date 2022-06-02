from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.urls.conf import include
from .views import HomeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('work.urls', namespace="work")),
    path('people/', include('people.urls', namespace="people")),
    path('place/', include('place.urls', namespace="place")),
    path('Products/', include('products.urls', namespace="Products")),


]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
