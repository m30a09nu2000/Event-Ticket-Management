from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import UserSerializer
from rest_framework.response import Response
from .models import UserData
from .user_utils.generarte_email import send_otp_via_email
from ticket_backend.utils.validators import (
    validate_email,
    validate_first_name,
    validate_last_name,
    validate_phone_number,
    validate_address,
    validate_password,
    validate_confirm,
)


class HomeView(APIView):
    def get(self, request):
        return Response("hii", status=201)


class RegisterView(APIView):

    def validate_user_details(self, data):
        email = data.get("email")
        validate_email_data = validate_email(email)
        if validate_email_data:
            return validate_email_data

        validate_first_name_data = validate_first_name(data.get("first_name"))
        if validate_first_name_data:
            return validate_first_name_data

        validate_last_name_data = validate_last_name(data.get("last_name"))
        if validate_last_name_data:
            return validate_last_name_data

        validate_phone_number_data = validate_phone_number(data.get("phone"))
        if validate_phone_number_data:
            return validate_phone_number_data

        validate_address_data = validate_address(data.get("address"))
        if validate_address_data:
            return validate_address_data

        validate_password_data = validate_password(data.get("password"))
        if validate_password_data:
            return validate_password_data

        validate_confirm_password_data = validate_confirm(
            data.get("confirm"), data.get("password")
        )
        if validate_confirm_password_data:
            return validate_confirm_password_data

    def post(self, request):
        validation_response = self.validate_user_details(request.data)

        if validation_response:
            return validation_response

        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            user = UserData.objects.get(email=request.data["email"])
            send_otp_via_email(user, 0)
            return Response(serializer.data, status=200)
        else:
            print(serializer.errors)
            return Response(
                {"error_code": "E100", "msg": serializer.errors},
                status=400,
            )
