from django.db import models
from stego_message.users.models import UserProfile
from django.utils.translation import ugettext_lazy as _


class Message(models.Model):
    sender = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='receiver')
    message = models.CharField(max_length=5000)
    encrytped_image = models.ImageField(upload_to='messages')
    timestamp = models.DateTimeField(auto_now_add=True)
    unread = models.BooleanField(default=True)

    class Meta:
        verbose_name = _("Message")
        verbose_name_plural = _("Messages")

    def __str__(self):
        return self.sender.user.username

    def get_absolute_url(self):
        return reverse("Message_detail", kwargs={"pk": self.pk})
