from rest_framework import generics
from .models import Duck
from .serializers import DuckSerializer, LoginSerializer
from django.shortcuts import get_object_or_404

from django.contrib.auth import login as django_login, logout as django_logout
#from django.shortcuts import render

# Create your views here.

class DuckList(generics.ListCreateAPIView):
	queryset = Duck.objects.all()
	serializer_class=DuckSerializer
	

	def get_object(self):
		queryset = self.get_queryset()
		obj=get_object_or_404(
			queryset,
			pk=self.kwargs['pk'],
		)
		return obj


from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from .serializers import LoginSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response

class LoginView(APIView):
	def post(self,request):
		print("  >> 1")
		serializer = LoginSerializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		user = serializer.validated_data["user"]
		django_login(request, user)
		Token, created  =Token.objects.get_or_create(user=user)

		print("  >> data: ")
		return Response({"token":token.key},status=200)


class LogoutView(APIView):
	authentication_classes = (TokenAuthentication,)

	def post(self, request):
		django_logout(request)
		return Response(status=204)

		
