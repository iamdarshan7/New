from django.urls import path
from .views import about, team, about_detail1, about_detail2, about_detail3, about_detail4, about_carousel_detail, testimonial

app_name = 'about_page' 

urlpatterns = [
    # path('', home, name="home"),
    # path('', PictureView.as_view(), name="pic"),
    path('about', about, name='about'),
    path('about/details1/', about_detail1, name='about_detail1'),
    path('about/details2/', about_detail2, name='about_detail2'),
    path('about/details3/', about_detail3, name='about_detail3'),
    path('about/details4/', about_detail4, name='about_detail4'),
    path('about/<int:pk>/', about_carousel_detail, name="about_carousel_detail"),
    path('about/testimonial/', testimonial, name="testimonial"),
    path('about/team/', team, name='team'),
]