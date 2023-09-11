from django.contrib.auth import get_user_model, update_session_auth_hash
from django.shortcuts import render, get_object_or_404
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from  rest_framework import status
from django.contrib.auth.hashers import check_password
from applications.account.serializers import RegisterSerializer, LoginSerializer

User = get_user_model()

class RegisterAPIView(APIView):
    def post(self,request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response('Вы успешно зарегистрировались. Вам отправлено письмо на почту с активацией',status=201)
    

class ActivationAPIView(APIView):
    def get(self, request, activation_code):
        # try:
        #     user = User.objects.get(activation_code=activation_code)
        # except User.DoesNotExist:
        #     return Response('Нет такого кода',status=400)
        user = get_object_or_404(User, activation_code=activation_code)
        user.is_active = True
        user.activation_code = ''
        user.save(update_fields=['is_active','activation_code'])
        return Response('Успешно', status=200)
    
# class LoginAPIView(ObtainAuthToken):
#     serializer_class = LoginSerializer


# class LogoutAPIView(APIView):
#     permission_classes = [IsAuthenticated]
#     def post(self, request):
#         token = Token.objects.get(user=request.user)
#         token.delete()
#         return Response('Вы успешно разлогинились', status=200)
    


class ChangePasswordAPIView(APIView):
    def post(self, request):
        email = request.data.get('email', '')
        current_password = request.data.get('current_password', '')
        new_password = request.data.get('new_password', '')
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response('Пользователь с такой почтой не найден', status=status.HTTP_400_BAD_REQUEST)
        if not user.check_password(current_password):
            return Response('Неверный текущий пароль', status=status.HTTP_400_BAD_REQUEST)
        if len(new_password) < 6:
            return Response('Новый пароль должен содержать не менее 6 символов', status=status.HTTP_400_BAD_REQUEST)
        user.set_password(new_password)
        user.save()
        update_session_auth_hash(request, user)
        return Response('Пароль успешно изменен', status=status.HTTP_200_OK)


