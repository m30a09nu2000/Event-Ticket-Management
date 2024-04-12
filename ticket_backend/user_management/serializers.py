from rest_framework import serializers
from .models import UserData


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserData
        fields = [
            "id",
            "email",
            "first_name",
            "last_name",
            "password",
            "phone",
            "address",
        ]

    def create(self, validated_data):
        user = UserData.objects.create(
            email=validated_data["email"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            phone=validated_data["phone"],
            address=validated_data["address"],
        )
        user.set_password(validated_data["password"])
        user.save()
        return user
