from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import TodoSerializer
from .models import TodoModel
from rest_framework import generics



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



class DetailApiView(generics.RetrieveUpdateDestroyAPIView):
    """
    this api for see and update and remove todo
    """
    queryset = TodoModel.objects.all().order_by('created')
    serializer_class = TodoSerializer


class StatsApiView(APIView): #TODO: fix this
    def get(self, request):
        user = request.user.id
        print(user)
        todo = TodoModel.objects.filter(user=user, is_done=True).count()
        return Response(f'your total done todo is: {todo}', status.HTTP_200_OK)
