from user_management.models import UserData
import re
from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import ValidationError
from .messages.error_messages import (
    error_code_e101,
    error_code_e102,
    error_code_e103,
    error_code_e104,
    error_code_e105,
    error_code_e106,
    error_code_e107,
    error_code_e108,
    error_code_e109,
    error_code_e110,
    error_code_e111,
    error_code_e112,
    error_code_e113,
    error_code_e114,
    error_code_e115,
    error_code_e116,
    error_code_e117,
    error_code_e118,
    error_code_e119,
)


def validate_email(email):
    if UserData.objects.filter(email=email).exists():
        return Response({"msg": error_code_e103()}, status=400)
    email_pattern = (
        r"^[a-zA-Z0-9][a-zA-Z0-9._%+-]{1,19}@[a-zA-Z0-9-]{1,25}(\.[a-zA-Z]{2,5})+$"
    )
    if not email:
        return Response({"msg": error_code_e101()}, status=400)
    if not re.match(email_pattern, email):
        return Response({"msg": error_code_e102()}, status=400)


def validate_first_name(first_name):
    if not first_name:
        return Response({"msg": error_code_e104()}, status=400)
    if len(first_name) < 3:
        return Response({"msg": error_code_e105()}, status=400)
    if len(first_name) > 30:
        return Response({"msg": error_code_e106()}, status=400)
    if not re.match(r"^[A-Za-z\s]{2,70}$", first_name):
        return Response({"msg": error_code_e107()}, status=400)
    if first_name.strip() != first_name:
        return Response({"msg": error_code_e108()}, status=400)
    return None


def validate_last_name(last_name):
    if not last_name:
        return Response({"msg": error_code_e109()}, status=400)
    if not re.match(r"^[A-Za-z\s]{2,70}$", last_name):
        return Response({"msg": error_code_e110()}, status=400)
    if last_name.strip() != last_name:
        return Response({"msg": error_code_e111()}, status=400)


def validate_phone_number(phone_number):
    if not phone_number:
        return Response({"msg": error_code_e112()}, status=400)
    pattern = r"^\d{10}$"
    if not re.match(pattern, phone_number):
        return Response({"msg": error_code_e113()}, status=400)
    if UserData.objects.filter(phone=phone_number).exists():
        return Response({"msg": error_code_e114()}, status=400)


def validate_address(address):
    if not address:
        return Response({"msg": error_code_e115()}, status=400)


E117 = error_code_e117()


def validate_password(password):
    special_characters = "!#$%&*?@_.-"

    if not password:
        return Response({"msg": error_code_e116()}, status=400)

    if len(password) < 8:
        return Response({"msg": E117["E117A"], "errorCode": "E117A"}, status=400)
    if len(password) > 15:
        return Response({"msg": E117["E117B"], "errorCode": "E117B"}, status=400)

    if not any(char in special_characters for char in password):
        return Response({"msg": E117["E117C"], "errorCode": "E117C"}, status=400)

    if not any(char.isupper() for char in password):
        return Response({"msg": E117["E117D"], "errorCode": "E117D"}, status=400)

    if not any(char.islower() for char in password):
        return Response({"msg": E117["E117E"], "errorCode": "E117E"}, status=400)

    if not any(char.isdigit() for char in password):
        return Response({"msg": E117["E117F"], "errorCode": "E117F"}, status=400)


def validate_confirm(confirm, password):
    if not confirm:
        return Response({"msg": error_code_e118()}, status=400)

    if confirm != password:
        return Response({"msg": error_code_e119()}, status=400)
