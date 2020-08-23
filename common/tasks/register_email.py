from .base_imports import *


def send_register_email(subject, message, to):
    send_mail(
        subject,
        message,
        settings.EMAIL_HOST_USER,
        to,
        fail_silently=False
    )