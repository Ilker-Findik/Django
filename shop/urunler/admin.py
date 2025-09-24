from django.contrib import admin
from .models import Kategoriler,Markalar
# Register your models here.

class KategoriAdmin(admin.ModelAdmin):
    list_display = ['isim','seo_title','slug','aktifMi']
    list_filter = ['aktifMi']
    search_fields = ['isim','seo_title']

admin.site.register(Kategoriler,KategoriAdmin)

class MarkalarAdmin(admin.ModelAdmin):
    list_display = ['isim','seo_title','slug','aktifMi','resim']
    list_filter = ['aktifMi']
    search_fields = ['isim','seo_title']

admin.site.register(Markalar,MarkalarAdmin)