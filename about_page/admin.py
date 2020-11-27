from django.contrib import admin
from .models import AboutMain, AboutCarousel, Teamsec1, Teamsec2, Testimonial, Navigation
# from .models import AboutSec1, AboutSec2, AboutSec3, AboutSec4, AboutSec5, AboutSec6, Teamsec1, Teamsec2
# Register your models here.

# admin.site.register(AboutSec1)
# admin.site.register(AboutSec2)
# admin.site.register(AboutSec3)
# admin.site.register(AboutSec4)
# admin.site.register(AboutSec5)
# admin.site.register(AboutSec6)

admin.site.register(Teamsec1)
admin.site.register(Teamsec2)
admin.site.register(AboutMain)
admin.site.register(AboutCarousel)
admin.site.register(Testimonial)
admin.site.register(Navigation)