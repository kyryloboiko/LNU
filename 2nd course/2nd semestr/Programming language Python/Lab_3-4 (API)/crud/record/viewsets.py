from rest_framework import generics
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .serializers import RecordSerializer
from .models import Records


class UpdateRecordApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Records.objects.all()
    serializer_class = RecordSerializer
    http_method_names = ['patch', 'put', 'delete', 'get','post', 'options']

    def get_object(self, *args, **kwargs):        
        return get_object_or_404(self.queryset, id=self.kwargs['id'])

class CreateRecordApiView(generics.ListCreateAPIView):
    serializer_class = RecordSerializer

    def get_queryset(self):
        return Records.objects.all()

    def list(self, request, *args, **kwargs):
        serializer = self.serializer_class
        queryset = self.get_queryset()

        return Response(serializer(queryset, many=True).data)

        
