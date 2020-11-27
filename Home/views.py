from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Pictures

# Create your views here.
def home(request):
    return render(request, "components/nav.html")

class PictureView(ListView):
    model = Pictures
    template_name = "index.html"
    # template_name = "Home/nav.html"
    # context['qs'] = Pictures.objects.filter(id=1)
    # return context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['logo'] = self.model.objects.all()
        return context

# def PictureView(models.Model):
#     context = {
#         'qs': Pictures.objects.filter(id=2)
#     }

#     return render(request, 'index.html', context)


# class PictureView(DetailView):
#     model = Pictures
#     template_name = "Home/index.html"
#     context_object_name = 'qs'