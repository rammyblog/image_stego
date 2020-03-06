from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from django.views.generic import DetailView, RedirectView, UpdateView
from .forms import UserCreationForm
from .utils import convert64toImage
from django.contrib.auth import authenticate, login,  logout

from .models import UserProfile

from django.http import HttpResponse

from functools import partial

from django.contrib.auth.decorators import login_required
from django_otp.forms import OTPTokenForm
from django_otp.plugins.otp_totp.models import TOTPDevice
from django_otp import user_has_device
from .qrcode_generator import barcodeGenerator


def userRegistration(request):

    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)

        if user_form.is_valid():
            user_form.save(commit=False)
            username = user_form.cleaned_data['username']
            password = user_form.cleaned_data['password1']
            user_form.save()
            user = authenticate(request, username=username, password=password)
            login(request, user)

            return redirect('users:user-image-registration')
    else:
        user_form = UserCreationForm()

    context = {
        'user_form': user_form
    }

    return render(request, 'account/signup.html', context)


def get_user_totp_device(request):
    user = request.user
    try:
        device = TOTPDevice.objects.get(user=user)
    except TOTPDevice.DoesNotExist:
        device = TOTPDevice.objects.create(user=user, confirmed=False, name='Google Auth')
    except TOTPDevice.MultipleObjectsReturned:
        device = TOTPDevice.objects.filter(user=user, confirmed=True)[:1]

    url = device.config_url
    barcode = barcodeGenerator(url)
    return render(request, 'account/totp_code.html', context={
        'url':url,
        'barcode':barcode
    })

def image_registration(request):
    if request.method == 'POST':
        image = request.POST['autentication_image']
        user_image = convert64toImage(image, request.user.username)
        user = get_object_or_404(UserProfile, user=request.user)
        user.autentication_image = user_image
        user.save()

        return redirect('users:otp-registration')

    # context = {
    #     'user':user
    # }

    return render(request, 'account/auth_image.html')


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        login(request, user)
        return HttpResponse('Login succesful')

    return render(request, 'account/login.html')


@login_required
def verify(request):
    if request.method == 'POST':
        token = request.POST['token']
        user = request.user
        device = TOTPDevice.objects.get(user=user)
        if device.verify_token(token):
            device.confirmed = True
            device.save()
            return HttpResponse('Verified')
        else:
            return HttpResponse('wrong token')

    return render(request, 'account/otp_auth_form.html')
    # return login(request, template_name='my_verify_template.html', authentication_form=form)
