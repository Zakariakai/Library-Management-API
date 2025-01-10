from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAccountOwner
from django.contrib.auth import get_user_model
from .serializers import UsersSerializer
from rest_framework.response import Response
from rest_framework import status
User = get_user_model()

class RegisterView(APIView):
    def post(self, request):
        """
        API endpoint to register a new user.

        Expects a POST request with the following data:
            - username
            - password
            - first_name
            - last_name
            - email

        Returns a 201 status code with a message saying the user was registered successfully if the request is valid.
        Returns a 400 status code with an error message if the request is invalid.

        :param request: The request object
        :return: A response object
        """
        username = request.data.get('username')
        password = request.data.get('password')
        email = request.data.get('email')
        first_name = request.data.get('first_name','')
        last_name = request.data.get('last_name','')
        if not username or not password or not email:
            return Response({'error': 'Please provide all required fields.'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            user = User.objects.create_user(username=username,email=email, password=password, first_name=first_name, last_name=last_name)
            return Response({'message': 'User registered successfully.'}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    def post(self, request):
        """
        Handle the login of a user.

        Args:
            request (Request): The request body with the user credentials.

        Returns:
            Response: A response with the result of the login and token.

        Raises:
            Exception: If the login of the user failed.
        """
        username = request.data.get('username')
        password = request.data.get('password')

        if not username or not password:
            return Response({'error':'Username and Password are required'}, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(request=request, username=username, password=password)

        if user is not None:

            token, created = Token.objects.get_or_create(user=user)
            return Response(
                {
                    'message':'Login successful',
                    'token': token.key
                },
                status=status.HTTP_200_OK
            )

        else:
            return Response({'error':'Invalid credentials.'}, status=status.HTTP_401_UNAUTHORIZED)


class LogoutView(APIView):
    def post(self, request):
        """
        API endpoint to logout an existing user.

        Expects a POST request.

        Returns a 200 status code with a message saying the logout was successful if the request is valid.
        Returns a 400 status code with an error message if the request is invalid.

        :param request: The request object
        :return: A response object
        """
        try:
           token = Token.objects.get(user=request.user)
           token.delete()
           return Response({'message': 'Logout successful.'}, status=status.HTTP_200_OK)
        except Token.DoesNotExist:
            return Response({'error': 'User is not logged in.'}, status=status.HTTP_400_BAD_REQUEST)
            


# API endpoint to retrieve, update, or delete a user
class UserAPIView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()  
    serializer_class = UsersSerializer
    lookup_field = 'username'
    permission_classes = [IsAuthenticated, IsAccountOwner]