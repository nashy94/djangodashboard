from django.contrib import admin
from django.urls import include, path
from dashboard import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('dashboard.urls')),
    path('accounts/',include('accounts.urls')),
    path('blog/', include('blog.urls')),
]
