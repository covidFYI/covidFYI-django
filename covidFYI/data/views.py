from django.shortcuts import render
# from rest_framework import generics
from rest_framework import viewsets
from .models import Location, Entry, InfoType
from .serializers import StateListSerializer, StateRetrieveSerializer, InfoTypeSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import generics

class StateViewSet(viewsets.ViewSet):
    permission_classes = [AllowAny]

    def list(self, request):

        queryset   = Location.objects.distinct('state')
        serializer = StateListSerializer(queryset, many=True)

        return Response(serializer.data)

    def retrieve(self, request, state_name):

        # locs_queryset = Location.objects.filter(state=state_name)
        locs_queryset = Location.objects.filter(state=state_name).order_by('district').prefetch_related('entries').all()
        # entries = Entry.objects.filter(location__in=locs_queryset)
        serializer = StateRetrieveSerializer(locs_queryset, many=True)

        return Response(serializer.data)

class InfoTypeViewSet(generics.ListAPIView):

    permission_classes = [AllowAny]
    queryset = InfoType.objects.all()
    serializer_class = InfoTypeSerializer

    # def get(self, request):
    #     queryset = self.get_queryset()
    #     import pdb; pdb.set_trace()
    #     serializer = InfoTypeSerializer(queryset, many=True)
    #     return Response(serializer.data)

# def IntoTypeListView(view.APIView):

#     def get(self, request)""