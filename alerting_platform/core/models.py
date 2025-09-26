from django.db import models
from django.contrib.auth.models import User, Group


class Team(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Alert(models.Model):
    INFO = 'info'
    WARNING = 'warning'
    CRITICAL = 'critical'
    SEVERITY_CHOICES = [(INFO, 'Info'), (WARNING, 'Warning'), (CRITICAL, 'Critical')]

    DELIVERY_IN_APP = 'in-app'
    DELIVERY_EMAIL = 'email'
    DELIVERY_SMS = 'sms'
    DELIVERY_PUSH = 'push'
    DELIVERY_CHOICES = [
        (DELIVERY_IN_APP, 'In-App'),
        (DELIVERY_EMAIL, 'Email'),
        (DELIVERY_SMS, 'SMS'),
        (DELIVERY_PUSH, 'Push Notification'),
    ]

    title = models.CharField(max_length=200)
    message = models.TextField()
    severity = models.CharField(max_length=10, choices=SEVERITY_CHOICES)
    start_time = models.DateTimeField()
    expiry_time = models.DateTimeField()
    reminder_frequency = models.IntegerField(default=120) # Minutes (customizable)
    delivery_type = models.CharField(max_length=50, choices=DELIVERY_CHOICES, default=DELIVERY_IN_APP)
    visible_to_org = models.BooleanField(default=False)
    teams = models.ManyToManyField(Team, blank=True)
    users = models.ManyToManyField(User, blank=True)
    archived = models.BooleanField(default=False)
    escalation_after = models.IntegerField(default=24*60)  # Minutes to escalate (default: 24h)
    escalated = models.BooleanField(default=False)
    cron_schedule = models.CharField(max_length=50, blank=True, help_text="Optional: cron pattern for scheduling")  # For scheduled alerts

    def __str__(self):
        return self.title


class NotificationDelivery(models.Model):
    alert = models.ForeignKey(Alert, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    delivered_at = models.DateTimeField(auto_now_add=True)
    delivery_channel = models.CharField(max_length=40, default='in-app')  # Track which channel was used

    def __str__(self):
        return f"{self.user} - {self.alert} - {self.delivery_channel}"


class UserAlertPreference(models.Model):
    alert = models.ForeignKey(Alert, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    read = models.BooleanField(default=False)
    snoozed_until = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.user} - {self.alert} - Read: {self.read}"


class PushSubscription(models.Model):
    """For web/mobile push notifications; store device token."""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    device_token = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.device_token}"


class RoleAccess(models.Model):
    """Role-based access for admin features"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=50)  # Could use Group model for more features
    features = models.JSONField(default=list)  # List of feature flags

    def __str__(self):
        return f"{self.user} - {self.role}"
