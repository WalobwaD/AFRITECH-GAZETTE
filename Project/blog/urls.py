from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

app_name = 'blog'

urlpatterns = [
    # path('', home_view, name="home"),
    path('', PostList.as_view(), name="home"),
    path('create/', create_view, name="create"),
    path('<slug>', PostDetails.as_view(), name="details"),
    
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)