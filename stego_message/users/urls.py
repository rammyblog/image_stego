from django.urls import path

from stego_message.users.views import (
    userRegistration,
    image_registration
    # user_redirect_view,
    # user_update_view,
)

app_name = "users"
urlpatterns = [
    path("register/", view=userRegistration, name="user-signp"),
    path("register/image", view=image_registration, name="user-image-registration"),

]
