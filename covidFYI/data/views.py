from django.shortcuts import render
from django.views.decorators.cache import cache_page
from django.core.cache import cache
from django.utils.decorators import method_decorator
from rest_framework import viewsets
from .models import Location, Entry, InfoType
from .serializers import StateListSerializer, StateRetrieveSerializer, InfoTypeSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import generics, views

VIEW_CACHE_TIME = 60*60

class StateViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [AllowAny]
    queryset = ''

    @method_decorator(cache_page(VIEW_CACHE_TIME))
    def list(self, request):

        queryset   = Location.objects.distinct('state')
        serializer = StateListSerializer(queryset, many=True)

        return Response(serializer.data)

    def retrieve(self, request, state_name):

        response = cache.get(state_name, None)
        if response is not None:
            return Response(response)
        
        locs_queryset = Location.objects.filter(state=state_name).order_by('district').prefetch_related('entries').all()
        serializer = StateRetrieveSerializer(locs_queryset, many=True)

        response = serializer.data
        cache.set(state_name, response, VIEW_CACHE_TIME)
        return Response(response)

class InfoTypeStatesView(views.APIView):

    permission_classes = [AllowAny]

    @method_decorator(cache_page(VIEW_CACHE_TIME))
    def get(self, request):

        response   = []
        info_types = InfoType.objects.all()

        for info_type in info_types:
            response.append({
                'info_type' : InfoTypeSerializer(info_type).data,
                'states'    : list(info_type.entries.distinct('location__state').\
                                    all().values_list('location__state', flat=True))
            })

        return Response(response)