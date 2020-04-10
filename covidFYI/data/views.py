from django.shortcuts import render
# from rest_framework import generics
from rest_framework import viewsets
from .models import Location, Entry, InfoType
from .serializers import StateListSerializer, StateRetrieveSerializer, InfoTypeSerializer, EntrySerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import generics, views

class StateViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [AllowAny]
    queryset = ''

    def list(self, request):

        queryset   = Location.objects.distinct('state')
        serializer = StateListSerializer(queryset, many=True)

        return Response(serializer.data)

    def retrieve(self, request, state_name):

        locs_queryset = Location.objects.filter(state=state_name).order_by('district').prefetch_related('entries').all()
        serializer = StateRetrieveSerializer(locs_queryset, many=True)

        return Response(serializer.data)

class InfoTypeRelatedData(views.APIView):

    permission_classes = [AllowAny]
    
    def get(self, request, state_name, info_type):
        queryset = Entry.objects.filter(location__state=state_name, infotype__name=info_type)
        serializer = EntrySerializer(queryset, many=True)
        return Response(serializer.data)

class InfoTypeStatesView(views.APIView):

    permission_classes = [AllowAny]

    def get(self, request):

        response   = []
        info_types = InfoType.objects.all()

        for info_type in info_types:
            response.append({
                'info_type' : info_type.name,
                'states'    : list(info_type.entries.distinct('location__state').\
                                    all().values_list('location__state', flat=True))
            })

        return Response(response)