# user_management/models.py
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

# Define the roles before using them
ROLES = [
    ('doctor', 'Doctor'),
    ('registration_clerk', 'Registration Clerk'),
    ('billing_staff', 'Billing Staff'),
    # Add other roles if necessary
]

class CustomUser(AbstractUser):
    contact = models.CharField(max_length=15, blank=True, null=True)
    role = models.CharField(max_length=50, choices=ROLES, blank=True, null=True)
    specialization = models.CharField(max_length=100, blank=True, null=True)

    # Add related fields for groups and permissions
    groups = models.ManyToManyField(Group, blank=True)
    user_permissions = models.ManyToManyField(Permission, blank=True)

    def __str__(self):
        return self.username

# user_management/models.py
from django.conf import settings  # Import settings

class Prescription(models.Model):
    patient = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    medication = models.CharField(max_length=255)
    dosage = models.CharField(max_length=255)
    instructions = models.TextField()

    def __str__(self):
        return f"Prescription for {self.patient.username} - {self.medication}"
# user_management/views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import CustomUser, Prescription
from django.contrib.auth.hashers import make_password

def add_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        contact = request.POST.get('contact')
        role = request.POST.get('role')
        specialization = request.POST.get('specialization')

        user = CustomUser(
            username=username,
            password=make_password(password),  # Hash the password
            contact=contact,
            role=role,
            specialization=specialization
        )
        user.save()
        messages.success(request, f'User {username} added successfully!')
        return redirect('user_list')
    return render(request, 'add_user.html')

def delete_user(request, user_id):
    try:
        user = CustomUser.objects.get(id=user_id)
        user.delete()
        messages.success(request, f'User {user.username} removed successfully!')
    except CustomUser.DoesNotExist:
        messages.error(request, 'User not found.')
    return redirect('user_list')

def user_list(request):
    users = CustomUser.objects.all()
    return render(request, 'user_list.html', {'users': users})
