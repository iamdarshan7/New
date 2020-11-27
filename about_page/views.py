from django.shortcuts import render
from .models import AboutMain, AboutCarousel, Teamsec1, Teamsec2, Testimonial, Navigation
# from .models import AboutSec1, AboutSec2, AboutSec3, AboutSec4, AboutSec5, AboutSec6, Teamsec1, Teamsec2
# from Home.models import Pictures
# Create your views here.

def team(request):
    objects1 = Teamsec1.objects.all()
    objects2 = Teamsec2.objects.all()
    objects3 = AboutCarousel.objects.all()
    objects4 = AboutMain.objects.all()
    logo = Navigation.objects.all()

    context = {
        'objects1': objects1,
        'objects2': objects2,
        'objects3': objects3,
        'objects4': objects4,
        'logo' : logo,
    }

    return render(request, 'team.html', context)



def about(request):
    objects1 = AboutMain.objects.all()
    objects2 = AboutCarousel.objects.all()
    logo = Navigation.objects.all()

    context = {
        'objects1' : objects1,
        'objects2' : objects2,
        'logo' : logo,
    }

    return render(request, 'about.html', context)



def about_detail1(request):
    sug = AboutMain.objects.all()
    logo = Navigation.objects.all()
    # objects2 = AboutCarousel.objects.all()

    context = {
        'sug' : sug,
        'logo' : logo,
        # 'objects2' : objects2
    }

    return render(request, 'about-detail1.html', context)




def about_detail2(request):
    sug = AboutMain.objects.all()
    logo = Navigation.objects.all()
    # objects2 = AboutCarousel.objects.all()

    context = {
        'sug' : sug,
        'logo' : logo,
        # 'objects2' : objects2
    }

    return render(request, 'about-detail2.html', context)





def about_detail3(request):
    sug = AboutMain.objects.all()
    logo = Navigation.objects.all()
    # objects2 = AboutCarousel.objects.all()

    context = {
        'sug' : sug,
        'logo' : logo,
        # 'objects2' : objects2
    }

    return render(request, 'about-detail3.html', context)





def about_detail4(request):
    sug = AboutMain.objects.all()
    logo = Navigation.objects.all()
    # objects2 = AboutCarousel.objects.all()

    context = {
        'sug' : sug,
        'logo' : logo,
        # 'objects2' : objects2
    }

    return render(request, 'about-detail4.html', context)





def about_carousel_detail(request, pk):
    sug = AboutCarousel.objects.get(id=pk)
    logo = Navigation.objects.all()

    context = {
        'sug' : sug,
        'logo' : logo,

    }

    return render(request, 'about-carousel-detail.html', context)




def testimonial(request):
    sug = Testimonial.objects.all()
    data = AboutCarousel.objects.all()
    data1 = AboutMain.objects.all()
    logo = Navigation.objects.all()

    context = {
        'sug': sug,
        "data": data,
        "data1": data1,
        'logo' : logo,
    }

    return render(request, 'testimonial.html', context)