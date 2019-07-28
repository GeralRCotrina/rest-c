from .models import Duck
from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from rest_framework import exceptions


class DuckSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model=Duck
		fields = ('id','duckname','ducklastname','duckemail','duckage')
			

class LoginSerializer(serializers.Serializer):
	
	username=serializers.CharField()
	password= serializers.CharField()

	def validate(self,data):
		print("  >> 21: ")
		username = data.get("username","")
		password = data.get("password","")

		if username and password:
			user = authenticate(username=username,password=password)
			if user:
				if user.is_active:
					data["user"]=user
				else:
					msg="Usuario desactivado."
					raise exceptions.validationError(msg)
			else:
				msg = "Sin credenciales."
				raise exceptions.validationError(msg)
		else:
			msg="Error en la utenticación."
			raise exceptions.validationError(msg)
		return data
		