from django.contrib.auth import get_user_model, authenticate
from django.utils.translation import ugettext_lazy as _
from rest_framework import serializers

# serializer는 직렬화하는 클래스로서, 사용자 모델 인스턴스를 json 혹은 dictionary형태로 직렬화할 수 있다.
# 만약 사용자 정보를 입력하는 URL이 /recipe/user/<user id>가 있고,
# 해당 view에는 user_id에 해당하는 모델 인스턴스의 정보를 리턴한다고 가정하자.
# 그렇게 되면 만약 우리가 /recipe/user/1/이라는 url로 요청했을 시
# user_id가 1인 사용자의 정보를 json형태로 응답받을 수 있다.
# 위와 같은 기능을 하는 serializer를 ModelSerializer라고 한다.

# 출처 : https://butter-shower.tistory.com/50

class UserSerializer(serializers.ModelSerializer):
    """Serializer for the users object"""

    class Meta:
        model=get_user_model()
        fields=('email', 'password', 'name')
        extra_kwargs={'password':{'write_only':True, 'min_length':5}}

    def create(self, validated_data):
        """Create a new user with encrypted password and return it"""
        return get_user_model().objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        """Update a user, setting the password correctly and return it"""
        password=validated_data.pop('password', None)
        user=super().update(instance, validated_data)

        if password:
            user.set_password(password)
            user.save()

        return user

class AuthTokenSerializer(serializers.Serializer):
    """Serializer for the user authentication object"""
    email=serializers.CharField()
    password=serializers.CharField(style={'input_type':'password'}, trim_whitespace=False)

    def validate(self, attrs):
        """Validate and authenticate the user"""
        email=attrs.get('email')
        password=attrs.get('password')

        user=authenticate(
            request=self.context.get('request'),
            username=email,
            password=password
        )
        if not user:
            msg=('Unable to authenticate with provided credentials')
            raise serializers.ValidationError(msg, code='authentication')

        attrs['user']=user
        return attrs
