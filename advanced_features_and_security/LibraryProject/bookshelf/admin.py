from django.contrib import admin
from .models import Book

# Register the Book model with the admin site
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # Customize the list display in the admin
    list_display = ('title', 'author', 'publication_year')
    
    # Add search functionality for title and author fields
    search_fields = ('title', 'author')
    
    # Add filter options for publication_year
    list_filter = ('publication_year',)

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'email', 'date_of_birth', 'profile_photo', 'is_staff')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email', 'date_of_birth', 'profile_photo')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
