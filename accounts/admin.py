from django.contrib import admin
from accounts.models import CustomUser

# Register your models here.
from accounts.models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['email','first_name','last_name','is_active','is_staff','is_superuser'] 
    readonly_fields = ('password',)