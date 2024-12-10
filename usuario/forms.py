from rest_framework import serializers
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
User = get_user_model()

class CustomUserCreationForm(serializers.ModelSerializer):
    password1 = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')
    
    
    def validate(self, data):
        # Validar que las contraseñas coincidan
        if data['password1'] != data['password2']:
            raise serializers.ValidationError({"password": "Las contraseñas no coinciden."})
        return data

    def create(self, validated_data):
        # Remover los campos de confirmación
        password = validated_data.pop('password1')
        validated_data.pop('password2')
        
        # Crear el usuario con la contraseña especificada
        user = User.objects.create_user(password=password, **validated_data)
        return user