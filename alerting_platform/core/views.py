from django.shortcuts import render, redirect, get_object_or_404
from .models import Alert, Team
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User

# Admin check
def is_admin(user):
    return user.is_staff

# Login view for admin
def admin_login(request):
    error = None
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_staff:
            login(request, user)
            return redirect('list_alerts')
        else:
            error = "Invalid login or not an admin."
    return render(request, 'core/login.html', {'error': error})

def admin_logout(request):
    logout(request)
    return redirect('admin_login')

@login_required
@user_passes_test(is_admin)
def list_alerts(request):
    alerts = Alert.objects.all().order_by('-start_time')
    return render(request, 'core/list_alerts.html', {'alerts': alerts})

@login_required
@user_passes_test(is_admin)
def create_alert(request):
    if request.method == 'POST':
        title = request.POST['title']
        message = request.POST['message']
        severity = request.POST['severity']
        start_time_str = request.POST.get('start_time')
        reminder_frequency = int(request.POST.get('reminder_frequency', 120))
        visible_to_org = 'visible_to_org' in request.POST
        team_ids = request.POST.getlist('teams')
        user_ids = request.POST.getlist('users')

        if start_time_str:
            start_time = timezone.datetime.fromisoformat(start_time_str)
            start_time = timezone.make_aware(start_time)
        else:
            start_time = timezone.now()
        expiry_time = start_time
        alert = Alert.objects.create(
            title=title,
            message=message,
            severity=severity,
            start_time=start_time,
            expiry_time=expiry_time,
            reminder_frequency=reminder_frequency,
            visible_to_org=visible_to_org
        )
        if team_ids:
            alert.teams.set(team_ids)
        if user_ids:
            alert.users.set(user_ids)

        messages.success(request, 'Alert created successfully!')
        return redirect('list_alerts')
    teams = Team.objects.all()
    users = User.objects.filter(is_active=True)
    return render(request, 'core/add_alert.html', {'teams': teams, 'users': users})

@login_required
@user_passes_test(is_admin)
def delete_alert(request, alert_id):
    alert = get_object_or_404(Alert, id=alert_id)
    if request.method == "POST":
        alert.delete()
        messages.success(request, "Alert deleted successfully!")
        return redirect('list_alerts')
    return render(request, 'core/confirm_delete.html', {'alert': alert})
