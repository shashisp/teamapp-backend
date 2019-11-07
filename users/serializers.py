from users.models import CustomUser
from rest_framework import serializers, exceptions


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['pk', 'first_name', 'last_name', 'phone', 'email', 'is_staff']

    def validate(self, data):
        username = data.get('email', None)
        if not self.instance:
            if CustomUser.objects.filter(email=username).exists():
                raise exceptions.ValidationError("Email already exists or invalid email")
            data["username"] = username
        else:
            user = CustomUser.objects.filter(email=username).first()
            if user and user.pk != self.instance.pk:
                raise exceptions.ValidationError("Email already exists")
        return data
