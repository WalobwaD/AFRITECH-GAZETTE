from django.urls import path
from .views import *
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('blogApi/', postApi.as_view(), name="blogApi"),
    path('blogApi/<slug:slug>/', postApiDetail.as_view(), name="blogApi"),
]
urlpatterns = format_suffix_patterns(urlpatterns)