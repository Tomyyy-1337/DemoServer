from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("speisekarte/", include("Speisekarte.urls")),
    path('apache-test/', include('apache_test.urls')),
    path("", include("Startseite.urls"))
]
