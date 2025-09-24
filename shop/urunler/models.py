from django.db import models
from django.db.models import ForeignKey


# Create your models here.

class Kategoriler(models.Model):
    isim = models.CharField(max_length=100)
    ustKategori = ForeignKey('self', on_delete=models.CASCADE,blank=True,null=True,
                             help_text="Eger bu kategori baska bir kategoriye bagliysa burayı doldurunuz.")
    aktifMi = models.BooleanField(default=True)
    seo_title = models.CharField(max_length=100,blank=True,null=True)
    seo_description = models.TextField(max_length=100,blank=True,null=True)
    slug = models.SlugField(max_length=100,unique=True,null=True,blank=True)

    class Meta:
        verbose_name_plural = 'Kategoriler'
        verbose_name = 'Kategoriler'

    def __str__(self):
        return self.isim

class Markalar(models.Model):
    isim = models.CharField(max_length=100)
    aciklama = models.TextField(blank=True,null=True)
    seo_title = models.CharField(max_length=100,blank=True,null=True)
    seo_description = models.TextField(max_length=100,blank=True,null=True)
    slug = models.SlugField(max_length=100,unique=True,null=True,blank=True)
    aktifMi = models.BooleanField(default=True)
    resim = models.ImageField(upload_to='markaresimleri',blank=True,null=True,)

    class Meta:
        verbose_name_plural = "Markalar"
        verbose_name = 'Marka'

    def __str__(self):
        return self.isim