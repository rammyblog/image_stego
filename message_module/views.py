from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import FormView, CreateView, UpdateView
from .models import Message
from .forms import SendMessageForm
from django.http import HttpResponse
from django.views.generic import ListView
from stego_message.users.models import UserProfile


class CreateMesageView(CreateView):
    model = Message
    form_class = SendMessageForm
    template_name = 'message_module/send_message.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     # context["messages"] = Message.objects.filter(sender=request.user)
    #     return context

    def form_valid(self, form):
        message = form.save()
        return render(self.request, '')


class SenderMessagesListView(ListView):
    model = Message
    template_name = 'message_module/messages.html'
    context_object_name = 'messages'

    def get_queryset(self):
        user = get_object_or_404(UserProfile, user=self.request.user)
        return Message.objects.filter(sender=user)
