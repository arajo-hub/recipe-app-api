from rest_framework import generics, authentication, permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from user.serializers import UserSerializer, AuthTokenSerializer

class CreateUserView(generics.CreateAPIView):
    """Create a new user in the system"""
    serializer_class=UserSerializer

class CreateTokenView(ObtainAuthToken):
    """Create a new auth token for user"""
    serializer_class=AuthTokenSerializer
    renderer_classes=api_settings.DEFAULT_RENDERER_CLASSES # Restframework의 default renderer classes 세팅을 이용하여 render한다.

# Before a TemplateResponse instance can be returned to the client, it must be rendered.
# The rendering process takes the intermediate representation of template and context,
# and turns it into the final byte stream that can be served to the client.

# 출처 : https://www.django-rest-framework.org/api-guide/renderers/

class ManageUserView(generics.RetrieveUpdateAPIView):
    """Manage the authenticated user"""
    serializer_class=UserSerializer
    authentication_classes=(authentication.TokenAuthentication,)
    permission_classes=(permissions.IsAuthenticated,)

    def get_object(self):
        """Retrieve and return authentication user"""
        return self.request.user
