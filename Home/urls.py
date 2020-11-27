from django.urls import path
from .views import home, PictureView

app_name = 'Home' 


urlpatterns = [
    # path('', home, name="home"),
    path('', PictureView.as_view(), name="pic"),
    # path('', PictureView, name="pic"),
    
]