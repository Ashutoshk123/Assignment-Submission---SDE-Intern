from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin-login/', views.admin_login, name='admin_login'),
    path('admin-logout/', views.admin_logout, name='admin_logout'),
    path('alerts/', views.list_alerts, name='list_alerts'),
    path('alerts/add/', views.create_alert, name='create_alert'),
    path('', views.list_alerts, name='home'),  # Homepage shows alerts!
    path('alerts/delete/<int:alert_id>/', views.delete_alert, name='delete_alert'),
]
