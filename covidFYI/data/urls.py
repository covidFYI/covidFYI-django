from django.urls import path, re_path, include, reverse_lazy
from .views import StateViewSet, InfoTypeStatesView, InfoTypeRelatedData

urlpatterns = [
    path('covidfyi/info_types/', InfoTypeStatesView.as_view()),
    path('covidfyi/states/', StateViewSet.as_view({'get' : 'list'})),
    path('covidfyi/states/<str:state_name>/<str:info_type>/', InfoTypeRelatedData.as_view()),
]