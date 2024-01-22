from django.contrib import admin
from userauths.models import User

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    """Setting up the admin style page in list form."""
    list_display = ['username', 'email', 'bio']

admin.site.register(User, UserAdmin)
