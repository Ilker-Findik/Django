from django.db import models
from django.db.models import ForeignKey
from django.contrib.auth.models import User


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

class Etiketler(models.Model):
    isim = models.CharField(max_length=100)
    aciklama = models.TextField(blank=True, null=True)
    aktifMi = models.BooleanField(default=True)
    slug = models.SlugField(max_length=100,unique=True,null=True,blank=True)
    class Meta:
        verbose_name_plural = "Etiketler"
        verbose_name = 'Etiket'

    def __str__(self):
        return self.isim

class Urunler (models.Model):
    isim = models.CharField(max_length=100)
    kullanici = models.ForeignKey(User, on_delete=models.CASCADE)
    fiyat = models.DecimalField(decimal_places=2, max_digits=10)
    marka =models.ForeignKey(Markalar, on_delete=models.CASCADE)
    kategori = models.ForeignKey(Kategoriler, on_delete=models.CASCADE)
    indirimli_fiyat = models.DecimalField(decimal_places=2, max_digits=10)
    kisa_aciklama = models.TextField(blank=True,null=True)
    aciklama = models.TextField(blank=True,null=True)
    seo_title = models.CharField(max_length=100,blank=True,null=True)
    seo_description = models.TextField(max_length=100,blank=True,null=True)
    slug = models.SlugField(max_length=100,unique=True,null=True,blank=True)
    aktifMi = models.BooleanField(default=True)
    resim = models.ImageField(upload_to='urunresimleri',blank=True,null=True,)
    tarih = models.DateTimeField(auto_now_add=True)
    etiketler = models.ManyToManyField(Etiketler,blank=True)

    class Meta:
        verbose_name_plural = 'Urunler'
        verbose_name = 'Urun'

    def __str__(self):
        return self.isim