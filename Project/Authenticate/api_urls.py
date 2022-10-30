from django.urls import path
from .views import *
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('userApi/', apiList.as_view(), name="apiList"),
    path('userApi/<int:pk>/', apiDetails.as_view(), name="apiDetail"),
]
urlpatterns = format_suffix_patterns(urlpatterns)