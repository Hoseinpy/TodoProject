from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import TodoSerializer
from .models import TodoModel
from rest_framework import generics


class List_Todo(APIView):
    """
    this api show all user todo
    """
    def get(self, request):
        try:
            todo = TodoModel.objects.filter(user=request.user)
            print(todo)
            serializer = TodoSerializer(todo, many=True)
            return Response(serializer.data, status.HTTP_200_OK)
        except:
            return Response({'status': 'need token'}, status.HTTP_401_UNAUTHORIZED)


class AddApiView(APIView):
    """
    this api for add todo
    """
    def post(self, request):
        try:
            serializer = TodoSerializer(data=request.data)
            if serializer.is_valid():
                todo = TodoModel.objects.create(user=request.user, name=serializer.data.get('name'), body=serializer.data.get('body'), is_done=serializer.data.get('is_done'))
                todo.save()
                return Response({'status': 'created'}, status.HTTP_201_CREATED)
            else:
                return Response({'status': 'bad request'}, status.HTTP_400_BAD_REQUEST)
        except:
            return Response({'status': 'need token'}, status.HTTP_401_UNAUTHORIZED)


class DetailApiView(generics.RetrieveUpdateDestroyAPIView):
    """
    this api for see and update and remove todo
    """    
    queryset = TodoModel.objects.all().order_by('created')
    serializer_class = TodoSerializer



class StatsApiView(APIView):
    """
    this api show is_done is True todo for user
    """
    def get(self, request):
        try:
            user = request.user
            todo = TodoModel.objects.filter(user=user, is_done=True).count()
            return Response(f'your done todo: {todo}', status.HTTP_200_OK)
        except:
            return Response({'status': 'need token'}, status.HTTP_401_UNAUTHORIZED)
