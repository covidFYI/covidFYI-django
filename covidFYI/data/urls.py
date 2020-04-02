from django.urls import path, re_path, include, reverse_lazy
from .views import StateViewSet, InfoTypeViewSet

urlpatterns = [
    path('covidfyi/states/', StateViewSet.as_view({'get' : 'list'})),
    path('covidfyi/info_types/', InfoTypeViewSet.as_view()),
    path('covidfyi/states/<str:state_name>/', StateViewSet.as_view({'get' : 'retrieve'}))
]