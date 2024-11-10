# from django.contrib import admin

# # Register your models here.
# # user_management/admin.py
# from django.contrib import admin
# # from .models import User

# # class UserAdmin(admin.ModelAdmin):
# #     list_display = ('username', 'role', 'specialization', 'contact')
# #     list_filter = ('role',)
# #     search_fields = ('username', 'role')

# # admin.site.register(User, UserAdmin)
# from django.contrib import admin
# from django.contrib.auth.models import User
# from django.contrib.auth.admin import UserAdmin

# # Unregister the default User model to avoid the AlreadyRegistered error
# admin.site.unregister(User)

# # Register the User model with any custom UserAdmin configurations you may need
# admin.site.register(User, UserAdmin)
# # from django.contrib import admin
# # from django.contrib.auth.models import User
# # from .models import CustomUser

# # Unregister the default User model (if you're replacing it)
# try:
#     admin.site.unregister(User)
# except admin.sites.NotRegistered:
#     pass  # If it's not registered, it will just pass without error

# # # Now register your custom user model
# # from django.contrib.auth.admin import UserAdmin
# # class CustomUserAdmin(UserAdmin):
# #     model = CustomUser
# #     list_display = ['username', 'email', 'contact', 'role', 'specialization']

# # # admin.site.register(CustomUser, CustomUserAdmin)
# # from django.contrib import admin
# # from django.contrib.auth.models import User
# # from .models import CustomUser   Import your CustomUser model

# # # Register your custom user model
# # from django.contrib.auth.admin import UserAdmin
# # class CustomUserAdmin(UserAdmin):
# #     model = CustomUser
# #     list_display = ['username', 'email', 'contact', 'role', 'specialization']  # Customize fields as needed

# # # Only register your custom model
# # admin.site.register(CustomUser, CustomUserAdmin)
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('role', 'specialization', 'contact')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('role', 'specialization', 'contact')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
