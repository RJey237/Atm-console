
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('atm_app.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
]
