from rest_framework import viewsets
from rest_framework.viewsets import ViewSet
from rest_framework import response
from .forms import CustomUserCreationForm
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import get_user_model


class viewsAPi(ViewSet):
    def post(request):
        try:
            serializer = CustomUserCreationForm(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return response({"mensage":serializer.data})
            else:
                return response({"message":"contraseña no coincide"})
        except Exception as e:
            print("error en", e)