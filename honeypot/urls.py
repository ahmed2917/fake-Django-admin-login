from django.urls import path, include
# from admin_honeypot.views import AdminHoneypot
# from django.contrib import admin
#
# urlpatterns = [
#
#     path('admins/', AdminHoneypot.as_view(), name='admin_honeypot'),
#     path('admin/login/', admin.site.urls),
#
# ]
# from django.urls import include, re_path

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    path(r'admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    path(r'secret/', admin.site.urls),
]