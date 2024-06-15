from django.urls import path
from tutorials import views as tutorials_views
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tutorials.urls')),
    path('', include('users.urls'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
