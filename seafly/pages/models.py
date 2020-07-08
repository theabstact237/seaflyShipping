from django.db import models
from django import forms


# Create your models here.

class Pages(models.Model):
    name = models.CharField(max_length=200, unique=True)
    title = models.CharField(max_length=200, unique=True)
    title_en = models.CharField(max_length=200, default='')
    title_th = models.CharField(max_length=200, default='')
    imgTop = models.CharField(max_length=200)
    imgRight = models.CharField(max_length=200)
    content = models.CharField(max_length=3000, default='')
    content_en = models.CharField(max_length=3000, default='')
    content_th = models.CharField(max_length=3000, default='')
    visibleImgRight = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=20)
    company = models.CharField(max_length=100)
    message = models.CharField(max_length=1000)


class devis(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=20)
    info_supp = models.CharField(max_length=500)
    date_expedition = models.CharField(max_length=30)
    transport_mode = models.CharField(max_length=20)
    livraison = models.CharField(max_length=255)
    livraison_country = models.CharField(max_length=30)
    dimension = models.CharField(max_length=255)
    type_emballage = models.CharField(max_length=30)
    volume = models.CharField(max_length=30)
    volume_unite = models.CharField(max_length=10)
    poids = models.CharField(max_length=30)
    poids_unite = models.CharField(max_length=10)
    marchandise = models.CharField(max_length=255)
    lieu_enlevement = models.CharField(max_length=255)
    enlevement_country = models.CharField(max_length=50)



class Pages_Form(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea)
    content_en = forms.CharField(widget=forms.Textarea)
    content_th = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Pages
        fields = '__all__'
