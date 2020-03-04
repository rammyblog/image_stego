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


def image_registration(request):
    if request.method == 'POST':
        image = request.POST['autentication_image']
        user_image = convert64toImage(image, request.user.username)
        user = get_object_or_404(UserProfile, user=request.user)
        user.autentication_image = user_image
        user.save()

        return HttpResponse('Photo successfully saved')

    # context = {
    #     'user':user
    # }

    return render(request, 'account/auth_image.html')
