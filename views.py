from django.shortcuts import render

# Create your views here.
# user_management/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import CustomUser
from .forms import CustomUserForm  # Change this to CustomUserForm

from django.contrib import messages


# user_management/views.py
from django.shortcuts import render

def roles(request):
    return render(request, 'user_management/roles.html')  # Adjust path to the template


from django.shortcuts import render

def index(request):
    return render(request, 'index.html')  # Ensure index.html exists in hm folder

# def add_user(request):
#     if request.method == 'POST':
#         form = UserForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "User added successfully!")
#             return redirect('user_list')
#     else:
#         form = UserForm()
#     return render(request, 'user_management/add_user.html', {'form': form})

# def remove_user(request, user_id):
#     user = get_object_or_404(User, id=user_id)
#     user.delete()
#     messages.success(request, "User removed successfully!")
#     return redirect('user_list')

# def user_list(request):
#     users = User.objects.all()
#     return render(request, 'user_management/user_list.html', {'users': users})
# # user_management/views.py
# import random
# from django.core.mail import send_mail
# from django.shortcuts import render, redirect
# from django.contrib import messages
# from django.urls import reverse
# from django.http import JsonResponse
# from .models import User  # Replace with the actual user model path in your project

# # Store OTPs temporarily (for demo purposes, it would be better to store in a database or cache in production)
# otp_store = {}
# user_management/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from .forms import CustomUserForm  # Assume you have a form for user creation

User = get_user_model()

def add_user(request):
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the user
            # If the role is 'doctor', automatically add to the doctor list
            if user.role == 'doctor':
                # Perform any extra operations here if needed (e.g., send a welcome email)
                print(f"New doctor added: {user.username}")
            return redirect('doctor_list')  # Redirect to the doctor list page
    else:
        form = CustomUserForm()
    return render(request, 'user_management/add_user.html', {'form': form})
# user_management/views.py
def doctor_list(request):
    # Fetch all users with the role 'doctor'
    doctors = User.objects.filter(role='doctor')
    return render(request, 'user_management/list_doctors.html', {'doctors': doctors})

# def send_otp(request):
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         phone = request.POST.get('phone')
        
#         # Check if user exists
#         try:
#             user = User.objects.get(email=email, phone=phone)
#         except User.DoesNotExist:
#             return JsonResponse({'error': 'User not found with this email and phone number.'}, status=404)

#         # Generate a 6-digit OTP
#         otp = random.randint(100000, 999999)
#         otp_store[email] = otp

#         # Send OTP to user's email
#         send_mail(
#             'Your OTP for Password Reset',
#             f'Your OTP is {otp}. It is valid for 5 minutes.',
#             'your-email@gmail.com',
#             [email],
#             fail_silently=False,
#         )

#         return JsonResponse({'message': 'OTP sent successfully! Please check your email.'})
    
#     return JsonResponse({'error': 'Invalid request method.'}, status=400)

# def reset_password(request):
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         otp = request.POST.get('otp')
#         new_password = request.POST.get('new_password')
        # user_management/views.py
def doctor_list(request):
    # Fetch all users with the role 'doctor'
    doctors = User.objects.filter(role='doctor')  # Assuming the role field is used for doctors
    return render(request, 'user_management/list_doctors.html', {'doctors': doctors})

#         # Verify OTP
#         if otp_store.get(email) == int(otp):
#             try:
#                 user = User.objects.get(email=email)
#                 user.set_password(new_password)  # For Django's default User model
#                 user.save()
                
#                 # Clear OTP after successful reset
#                 del otp_store[email]

#                 return JsonResponse({'message': 'Password reset successful!'})
#             except User.DoesNotExist:
#                 return JsonResponse({'error': 'User not found.'}, status=404)
#         else:
#             return JsonResponse({'error': 'Invalid OTP.'}, status=400)
    
#     return JsonResponse({'error': 'Invalid request method.'}, status=400)

def admin_add_remove_user(request):
    return render(request, 'admin_add_remove_user.html')

def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')

def admin_financial_report_response(request):
    return render(request, 'admin_financial_report_response.html')

def admin_login(request):
    return render(request, 'admin_login.html')

def admin_logout(request):
    return render(request, 'admin_logout.html')

def admin_request_financial_report(request):
    return render(request, 'admin_request_financial_report.html')

def admin_review_feedback(request):
    return render(request, 'admin_review_feedback.html')

def billing_staff_dashboard(request):
    return render(request, 'billing_staff_dashboard.html')

def billing_staff_login(request):
    return render(request, 'billing_staff_login.html')

def billing_staff_logout(request):
    return render(request, 'billing_staff_logout.html')

def cancel_appointments(request):
    return render(request, 'cancel_appointments.html')

def check_doctor_availability(request):
    return render(request, 'check_doctor_availability.html')

def doctor_availability(request):
    return render(request, 'doctor_availability.html')

def doctor_dashboard(request):
    return render(request, 'doctor_dashboard.html')

def doctor_login(request):
    return render(request, 'doctor_login.html')

def forgot_password(request):
    return render(request, 'forgot_password.html')

def registration_clerk_logout(request):
    return render(request, 'registration_clerk_logout.html')

def fpass_billStaff(request):
    return render(request, 'fpass_billStaff.html')

def fpas_admin(request):
    return render(request, 'fpas_admin.html')

def fpas_doctor(request):
    return render(request, 'fpas_doctor.html')

def fpas_regcler(request):
    return render(request, 'fpas_regcler.html')

def generate_bill(request):
    return render(request, 'generate_bill.html')

def give_prescription(request):
    return render(request, 'user_management/give_prescription.html')

def index(request):
    return render(request, 'index.html')

def list_doctors(request):
    return render(request, 'list_doctors.html')

def logout_view(request):
    return render(request, 'logout.html')

def make_appointment(request):
    return render(request, 'make_appointment.html')

def medical_records(request):
    return render(request, 'medical_records.html')

def patient_dashboard(request):
    return render(request, 'patient_dashboard.html')

def patient_login(request):
    return render(request, 'patient_login.html')

def patient_sign_up(request):
    return render(request, 'patient_sign_up.html')

def process_payment(request):
    return render(request, 'process_payment.html')

def register_patient(request):
    return render(request, 'register_patient.html')

def registration_clerk_dashboard(request):
    return render(request, 'registration_clerk_dashboard.html')

def registration_clerk_login(request):
    return render(request, 'registration_clerk_login.html')

def request_financial_report(request):
    return render(request, 'request_financial_report.html')

def request_invoice(request):   
    return render(request, 'request_invoice.html')

def request_medical_history(request):
    return render(request, 'request_medical_history.html')

def roles(request):
    return render(request, 'roles.html')

def doctor_logout(request):
    return render(request, 'doctor_logout.html')

def sign_up(request):
    return render(request, 'sign_up.html')

def submit_feedback(request):
    return render(request, 'submit_feedback.html')

def update_patient_info(request):
    return render(request, 'update_patient_info.html')

def update_patient_status(request):
    return render(request, 'update_patient_status.html')

def verify_otp(request):
    return render(request, 'verify_otp.html')

def view_appointments(request):
    return render(request, 'view_appointments.html')

def view_prescriptions(request):
    return render(request, 'view_prescriptions.html')

# user_management/views.py
from django.shortcuts import render, redirect
from .forms import CustomUserForm
from .models import CustomUser  # Assuming you have a custom User model

def add_user(request):
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()  # This will create a new user with the specified 'username' and 'role'
            return redirect('user_management:admin_dashboard')  # Redirect after successful form submission
    else:
        form = CustomUserForm()
    
    return render(request, 'user_management/add_user.html', {'form': form})

# user_management/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import CustomUser

def remove_user(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    if request.method == 'POST':
        user.delete()  # Delete the user
        return redirect('user_management:admin_dashboard')  # Redirect to admin dashboard after deletion
    
    return render(request, 'user_management/remove_user.html', {'user': user})


# # user_management/views.py
# from django.shortcuts import render, redirect
# from django.contrib.auth.decorators import login_required
# from .models import User
# from .forms import UserForm

# # Admin view to list all doctors
# @login_required
# def list_doctors(request):
#     doctors = User.objects.filter(role='doctor')
#     return render(request, 'list_doctors.html', {'doctors': doctors})

# # Admin view to add or remove users (doctors)
# @login_required
# def admin_manage_doctors(request):
#     if request.user.role !=  'admin':
#         return redirect('home')  # Redirect non-admin users

#     if request.method == 'POST':
#         form = UserForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('admin_manage_doctors')  # Redirect after adding doctor
#     else:
#         form = UserForm()

#     doctors = User.objects.filter(role='doctor')

#     return render(request, 'admin_manage_doctors.html', {'form': form, 'doctors': doctors})

# # user_management/views.py
# from django.shortcuts import get_object_or_404

# # @login_required
# # def remove_doctor(request, id):
# #     if request.user.role != 'admin':
# #         return redirect('home')  # Redirect non-admin users

# #     doctor = get_object_or_404(User, id=id)
# #     doctor.delete()  # Delete the doctor from the database
# #     return redirect('admin_manage_doctors')


# # # user_management/views.py
# # @login_required
# # def list_doctors(request):
# #     doctors = User.objects.filter(role='doctor')
# #     return render(request, 'list_doctors.html', {'doctors': doctors})
# from django.shortcuts import render, redirect
# from .forms import PrescriptionForm
# from .models import Prescription
# from django.contrib.auth.decorators import login_required

# @login_required
# def give_prescription(request):
#     if request.method == 'POST':
#         form = PrescriptionForm(request.POST)
#         if form.is_valid():
#             prescription = form.save(commit=False)
#             prescription.doctor = request.user
#             prescription.save()
#             return redirect('doctor_dashboard')  # Redirect to doctor dashboard after saving
#     else:
#         form = PrescriptionForm()
#     return render(request, 'give_prescription.html', {'form': form})

# @login_required
# def view_prescriptions(request):
#     prescriptions = Prescription.objects.filter(patient=request.user)
#     return render(request, 'view_prescriptions.html', {'prescriptions': prescriptions})
# user_management/views.py

from django.shortcuts import render

def give_prescription(request):
    return render(request, 'give_prescription.html')


from django.shortcuts import render, redirect
from .forms import PrescriptionForm

def give_prescription(request):
    if request.method == 'POST':
        form = PrescriptionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_prescriptions')  # Redirect after saving the prescription
    else:
        form = PrescriptionForm()

    return render(request, 'user_management/give_prescription.html', {'form': form})



def prescribe(request):
    return render(request, 'prescribe.html')

# user_management/views.py
from django.shortcuts import render
from .models import CustomUser

def user_list(request):
    users = CustomUser.objects.all()
    return render(request, 'user_list.html', {'users': users})


# user_management/views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import CustomUser
from django.contrib.auth.hashers import make_password

@login_required
def add_user(request):
    # Restrict access to admin users only
    if request.user.role != 'admin':
        messages.error(request, "You do not have permission to add users.")
        return redirect('user_list')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        contact = request.POST.get('contact')
        role = request.POST.get('role')
        specialization = request.POST.get('specialization')

        user = CustomUser(
            username=username,
            password=make_password(password),
            contact=contact,
            role=role,
            specialization=specialization
        )
        user.save()
        messages.success(request, f'User {username} added successfully!')
        return redirect('user_list')
    
    return render(request, 'add_user.html')

@login_required
def remove_user(request, user_id):
    # Restrict access to admin users only
    if request.user.role != 'admin':
        messages.error(request, "You do not have permission to remove users.")
        return redirect('user_list')
    
    try:
        user = CustomUser.objects.get(id=user_id)
        user.delete()
        messages.success(request, f'User {user.username} removed successfully!')
    except CustomUser.DoesNotExist:
        messages.error(request, 'User not found.')
    
    return redirect('user_list')

@login_required
def user_list(request):
    users = CustomUser.objects.all()
    return render(request, 'user_list.html', {'users': users})
