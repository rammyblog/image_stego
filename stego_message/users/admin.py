from django.contrib import admin
from .models import UserProfile
# from django.contrib.auth import admin as auth_admin
# from django.contrib.auth import get_user_model

# from stego_message.users.forms import UserChangeForm, UserCreationForm

# User = get_user_model()


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ["user"]
    search_fields = ["user"]
