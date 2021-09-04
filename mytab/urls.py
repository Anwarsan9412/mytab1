from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('',include('accounts.urls')),
#     path('tabungan/', include('tabungan.urls')),
#     path('pinjaman/', include('pinjaman.urls')),
]
