from django.forms import ModelForm, Textarea
from .models import Message
from django.db import transaction
from .imageStegoAlgo import encode


class SendMessageForm(ModelForm):

    class Meta:
        model = Message
        exclude = ['encrytped_image']

    @transaction.atomic
    def save(self):
        data = self.cleaned_data
        message = data['message']
        sender = data['sender']
        print(data)
        message_object = super().save(commit=False)
        print(message_object)
        image_url = encode(message, sender, message_object.id)
        message_object.encrytped_image = image_url
        message_object.save()
        return message_object
