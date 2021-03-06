from .models import User
from rest_framework.serializers import ModelSerializer

class AccountSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'id', 'password', 'name']

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

class UserViewSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'name', 'is_educator', 'is_student']
