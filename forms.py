# user_management/forms.py
from django import forms
 # Assuming you have a custom User model


# # user_management/forms.py
# from django import forms
# from .models import User

# class UserForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ['username', 'role', 'specialization', 'contact']

# from django.shortcuts import render, redirect


# def add_user(request):
#     if request.method == 'POST':
#         form = UserForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('doctor_list')  # Redirect to the list of doctors page
#     else:
#         form = UserForm()

#     return render(request, 'user_management/add_user.html', {'form': form})

from django import forms
from .models import Prescription

class PrescriptionForm(forms.ModelForm):
    class Meta:
        model = Prescription
        fields = ['patient', 'medication', 'dosage', 'instructions']

from django import forms
from .models import CustomUser  # Import CustomUser from models

class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'role', 'specialization', 'contact']

