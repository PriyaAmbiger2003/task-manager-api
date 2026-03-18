from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny  # ✅ ADD THIS
from .serializers import RegisterSerializer


class RegisterView(APIView):

    permission_classes = [AllowAny]   # ✅ VERY IMPORTANT

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User registered successfully"}, status=201)

        return Response(serializer.errors, status=400)