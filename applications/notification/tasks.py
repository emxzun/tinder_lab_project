from config.celery import app
from django.core.mail import send_mail


@app.task
def send_notification_like(email, notification_like):
    send_mail(
        'This person liked you',
        f'{notification_like}',
        'kadirbekova43@gmail.com',
        [email]
    )
@app.task
def send_notification_chat(email, notification_chat):
    send_mail(
        'This person want to chat with yoo',
        f'{notification_chat}',
        'kadirbekova43@gmail.com',
        [email]
    )
