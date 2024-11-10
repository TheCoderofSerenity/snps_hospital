# user_management/urls.py
from django.urls import path
from . import views


from django.contrib import admin
from django.urls import include, path
from user_management import views  # Import the index view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user_management/', include('user_management.urls')),
    path('', views.index, name='home'),  # Set the root URL to display the homepage
]
from django.urls import path
from user_management import views  # Import views from user_management

urlpatterns = [
    path('give_prescription/', views.give_prescription, name='give_prescription'),  # Adjust the URL
    # other patterns
]

urlpatterns = [
    path('admin_add_remove_user/', views.admin_add_remove_user, name='admin_add_remove_user'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('admin_financial_report_response/', views.admin_financial_report_response, name='admin_financial_report_response'),
    path('admin_login/', views.admin_login, name='admin_login'),
    path('admin_request_financial_report/', views.admin_request_financial_report, name='admin_request_financial_report'),
    path('admin_review_feedback/', views.admin_review_feedback, name='admin_review_feedback'),
    path('admin_logout/', views.admin_logout, name='admin_logout'),
    path('billing_staff_dashboard/', views.billing_staff_dashboard, name='billing_staff_dashboard'),
    path('billing_staff_login/', views.billing_staff_login, name='billing_staff_login'),
    path('cancel_appointments/', views.cancel_appointments, name='cancel_appointments'),
    path('check_doctor_availability/', views.check_doctor_availability, name='check_doctor_availability'),
    path('doctor_dashboard/', views.doctor_dashboard, name='doctor_dashboard'),
    path('doctor_login/', views.doctor_login, name='doctor_login'),
    path('forgot_password/', views.forgot_password, name='forgot_password'),
    path('fpass_billStaff/', views.fpass_billStaff, name='fpass_billStaff'),
    path('prescribe/', views.prescribe, name='prescribe'),
    path('fpas_admin/', views.fpas_admin, name='fpas_admin'),
    path('fpas_doctor/', views.fpas_doctor, name='fpas_doctor'),
    path('doctor_logout/', views.doctor_logout, name='doctor_logout'),
    path('fpas_regcler/', views.fpas_regcler, name='fpas_regcler'),
    path('generate_bill/', views.generate_bill, name='generate_bill'),
    path('', views.index, name='index'),  # Homepage view
    path('list_doctors/', views.list_doctors, name='list_doctors'),
    path('logout/', views.logout_view, name='logout'),
    path('make_appointment/', views.make_appointment, name='make_appointment'),
    path('medical_records/', views.medical_records, name='medical_records'),
    path('patient_dashboard/', views.patient_dashboard, name='patient_dashboard'),
    path('patient_login/', views.patient_login, name='patient_login'),
    path('patient_sign_up/', views.patient_sign_up, name='patient_sign_up'),
    path('process_payment/', views.process_payment, name='process_payment'),
    path('register_patient/', views.register_patient, name='register_patient'),
    path('registration_clerk_dashboard/', views.registration_clerk_dashboard, name='registration_clerk_dashboard'),
    path('registration_clerk_login/', views.registration_clerk_login, name='registration_clerk_login'),
    path('registration_clerk_logout/', views.registration_clerk_logout, name='registration_clerk_logout'),
    path('request_financial_report/', views.request_financial_report, name='request_financial_report'),
    path('request_invoice/', views.request_invoice, name='request_invoice'),
    path('request_medical_history/', views.request_medical_history, name='request_medical_history'),
    path('roles/', views.roles, name='roles'),
    path('sign_up/', views.sign_up, name='sign_up'),
    path('submit_feedback/', views.submit_feedback, name='submit_feedback'),
    path('update_patient_info/', views.update_patient_info, name='update_patient_info'),
    path('update_patient_status/', views.update_patient_status, name='update_patient_status'),
    path('verify_otp/', views.verify_otp, name='verify_otp'),
    path('billing_staff_logout/', views.billing_staff_logout, name='billing_staff_logout'),
    path('view_appointments/', views.view_appointments, name='view_appointments'),
    path('view_prescriptions/', views.view_prescriptions, name='view_prescriptions'),
     path('', views.index, name='home'),
]
# user_management/urls.py
from django.urls import path
from . import views

urlpatterns = [

    path('roles/', views.roles, name='roles.html'),  # This should be correct
]
# user_management/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('add_user/', views.add_user, name='add_user'),
    path('/', views.doctor_list, name='doctor_list'),
]

# user_management/urls.py
from django.urls import path
from . import views

app_name = 'user_management'

urlpatterns = [
    path('add_user/', views.add_user, name='add_user'),  # URL for adding users
    path('remove_user/<int:user_id>/', views.remove_user, name='remove_user'),  # URL for removing users
]
# user_management/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('list_doctors/', views.doctor_list, name='doctor_list'),  # URL for the doctor list page
    path('patient_dashboard/', views.patient_dashboard, name='patient_dashboard'),
    path('doctor_availability.html', views.doctor_availability, name='doctor_availability'),
# ]
# # user_management/urls.py
# from django.urls import path
# from . import views

# urlpatterns = [
#     path('list_doctors/', views.list_doctors, name='list_doctors'),  # Patient's view
#     path('admin/manage_doctors/', views.admin_manage_doctors, name='admin_manage_doctors'),
#     # Add a URL for removing a doctor
#     # path('remove_doctor/<int:id>/', views.remove_doctor, name='remove_doctor'),
]
# user_management/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('list_doctors/', views.list_doctors, name='list_doctors'),
    path('admin_add_remove_user/', views.admin_add_remove_user, name='admin_add_remove_user'),
    path('remove_user/<int:user_id>/', views.remove_user, name='remove_user'),
]
# user_management/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('add_user.html', views.add_user, name='add_user'),
    path('remove_user.html', views.remove_user, name='delete_user'),
    path('user_list.html', views.user_list, name='user_list'),
]
