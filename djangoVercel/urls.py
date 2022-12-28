from django.contrib import admin
from django.urls import path, include

from example import urls as eUrls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(eUrls)),
]
