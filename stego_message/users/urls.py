from django.urls import path

from stego_message.users.views import (
    userRegistration,
    image_registration,
    user_login,
    verify,
    get_user_totp_device
    # user_redirect_view,
    # user_update_view,
)

app_name = "users"
urlpatterns = [
    path("register/", view=userRegistration, name="user-sigup"),
    path("register/image", view=image_registration, name="user-image-registration"),
    path("login/", view=user_login, name="user-login"),
    path("login/verify", view=verify, name="user-login-verify"),
    path('otp/registration/', view=get_user_totp_device, name='otp-registration')




]
