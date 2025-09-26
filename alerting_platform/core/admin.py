from django.contrib import admin
from .models import Team, Alert, NotificationDelivery, UserAlertPreference

admin.site.register(Team)
admin.site.register(Alert)
admin.site.register(NotificationDelivery)
admin.site.register(UserAlertPreference)
