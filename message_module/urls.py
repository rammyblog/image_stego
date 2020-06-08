from django.urls import path

from .views import (CreateMesageView, SenderMessagesListView)

app_name = "messages"

urlpatterns = [
    path('create/', CreateMesageView.as_view(), name='create-message'),
    path('all/', SenderMessagesListView.as_view(), name='all-message')

]
