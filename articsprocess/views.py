from .models import Text
from rest_framework import status
from .serializers import UserProfileSerializer, SearchHistorySerializer
from rest_framework.response import Response
from rest_framework.views import APIView
# from moduleProcess.receiverData import moduleProcess


class Register(APIView):
    def get(self, request):
        query = Text.objects.order_by('id').reverse()[:1]
        serializer = UserProfileSerializer(query, many=True)
        # instance = moduleProcess(query=serializer.data)
        return Response(serializer.data) 

    def post(self, request):
        serializer = UserProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

class Data(APIView):
    def get(self, request):
        query = Text.objects.order_by('id').reverse()[:1]
        serializer = SearchHistorySerializer(query, many=True)
        # instance = moduleProcess(query=serializer.data)
        return Response(serializer.data) 

    def post(self, request):
        serializer = SearchHistorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

    def put(self, request):
        pass
    



