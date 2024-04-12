from django.core.mail import send_mail
import random
from django.conf import settings
from user_management.models import OtpData
from django.utils import timezone


def send_otp_via_email(email, type):
    otp = random.randint(1000, 9999)
    print(type)
    print(otp)
    if type == 0:
        subject = "Verify Email"
        message = f"Dear user, your OTP for email address verification is {otp}.\nValid for the next 5 minutes"

    email_from = settings.EMAIL_HOST
    send_mail(subject, message, email_from, [email])
    otp_data = OtpData.objects.filter(userid=email).first()
    if otp_data and otp_data.otp == otp:
        otp_data.status = 1
        otp_data.save()
    else:
        OtpData.objects.create(userid=email, otp=otp, timestamp=timezone.now())
