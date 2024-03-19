from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import TodoSerializer
from .models import TodoModel



class AddApiView(APIView):
    """
    this api for add todo
    """
    def post(self, request):
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'created'}, status.HTTP_201_CREATED)
        else:
            return Response({'status': 'bad request'}, status.HTTP_400_BAD_REQUEST)



class DetailApiView(APIView):
    """
    this api for see and update and remove todo
    """
    def get(self, request):
        pass

    def put(self, request):
        pass

    def delete(self, request):
        pass
