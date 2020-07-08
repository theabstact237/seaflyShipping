from django.contrib import admin
from .models import Pages, Pages_Form


# Register your models here.
class PagesAdmin(admin.ModelAdmin):
    form = Pages_Form
    list_display = ('name', 'title', 'imgTop', 'imgRight', 'content', 'visibleImgRight')


admin.site.site_header = 'Page d\'administration'
admin.site.register(Pages, PagesAdmin)
