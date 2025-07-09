from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import SignupSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg.openapi import Parameter, IN_HEADER

class SignupView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(request_body=SignupSerializer)
    def post(self, request):
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'User created successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MeView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        manual_parameters=[
            Parameter('Authorization', IN_HEADER, description="JWT Token like: Bearer <access_token>", type='string')
        ]
    )
    def get(self, request):
        user = request.user
        return Response({
            'id': user.id,
            'name': user.name,
            'username': user.username,
            'email': user.email,
            'phone': user.phone,
        })

