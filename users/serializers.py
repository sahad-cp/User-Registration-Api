from rest_framework import serializers
from .models import User


class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name', 'email', 'date_joined','password', 'is_active']
        
        extra_kwargs = {
            'password' : {'write_only' : True}
        }
        
    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        password=self.validated_data['password']
        user.set_password(password)
        user.save()
        return user    
    


class UserLoginSerializer(serializers.ModelSerializer):
  email = serializers.EmailField(max_length=255)
  class Meta:
    model = User
    fields = ['email', 'password']
    
    
class UserChangePasswordSerializer(serializers.Serializer):
  password = serializers.CharField(max_length=255, style={'input_type':'password'}, write_only=True)
  password2 = serializers.CharField(max_length=255, style={'input_type':'password'}, write_only=True)
  class Meta:
    fields = ['password', 'password2']

  def validate(self, attrs):
    password = attrs.get('password')
    password2 = attrs.get('password2')

    user = self.context.get('user')

    if user.check_password(password):
      user.set_password(password2)
      user.save()

    else:
      raise serializers.ValidationError("Password wrong")
    return attrs

class UserProfileSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ['id', 'email', 'name','is_banned']