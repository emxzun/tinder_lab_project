from django.contrib import admin

<<<<<<< HEAD
from applications.chat.models import Room

admin.site.register(Room)
=======
from applications.chat.models import Chat, Message

admin.site.register(Chat)
admin.site.register(Message)
>>>>>>> origin/mika
