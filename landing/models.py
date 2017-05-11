from __future__ import unicode_literals
from  mezzanine.core import  fields
from mezzanine.pages.models import Page

from django.db import models

DATASET_TYPES = [
    ('Voters', 'Voters'),
    ('Candidates', 'Candidates'),
    ('Political Parties', 'Political Parties'),
    ('Federal', 'Federal'),
    ('Results', 'Results'),
    ('Others', 'Others'),
]
DISTRICT = [
    ('Achham ', 'Achham'),
    ('Arghakhanchi', 'Arghakhanchi'),
    ('Baglung', 'Baglung'),
    ('Baitadi', 'Baitadi'),
    ('Bajhang', 'Bajhang'),
    ('Bajura', 'Bajura'),
    ('Banke', 'Banke'),
    ('Bara', 'Bara'),
    ('Bardiya', 'Bardiya'),
    ('Bhaktapur', 'Bhaktapur'),
    ('Bhojpur', 'Bhojpur'),
    ('Chitwan', 'Chitwan'),
    ('Dadeldhura', 'Dadeldhura'),
    ('Dailekh', 'Dailekh'),
    ('Dang', 'Dang'),
    ('Darchula', 'Darchula'),
    ('Dhading', 'Dhading'),
    ('Dhankuta', 'Dhankuta'),
    ('Dhanusa', 'Dhanusa'),
    ('Dolakha', 'Dolakha'),
    ('Dolpa', 'Dolpa'),
    ('Doti', 'Doti'),
    ('Gorkha', 'Gorkha'),
    ('Gulmi', 'Gulmi'),
    ('Humla', 'Humla'),
    ('Ilam', 'Ilam'),
    ('Jajarkot', 'Jajarkot'),
    ('Jhapa', 'Jhapa'),
    ('Jumla', 'Jumla'),
    ('Kailali', 'Kailali'),
    ('Kalikot', 'Kalikot'),
    ('Kanchanpur', 'Kanchanpur'),
    ('Kapilbastu', 'Kapilbastu'),
    ('Kaski', 'Kaski'),
    ('Kathmandu', 'Kathmandu'),
    ('Kavrepalanchok', 'Kavrepalanchok'),
    ('Khotang', 'Khotang'),
    ('Lalitpur', 'Lalitpur'),
    ('Lamjung', 'Lamjung'),
    ('Mahottari', 'Mahottari'),
    ('Makwanpur', 'Makwanpur'),
    ('Manang', 'Manang'),
    ('Morang', 'Morang'),
    ('Mugu', 'Mugu'),
    ('Mustang', 'Mustang'),
    ('Myagdi', 'Myagdi'),
    ('Nawalparasi', 'Nawalparasi'),
    ('Nuwakot', 'Nuwakot'),
    ('Okhaldhunga', 'Okhaldhunga'),
    ('Palpa', 'Palpa'),
    ('Panchthar', 'Panchthar'),
    ('Parbat', 'Parbat'),
    ('Parsa', 'Parsa'),
    ('Pyuthan', 'Pyuthan'),
    ('Ramechhap', 'Ramechhap'),
    ('Rasuwa', 'Rasuwa'),
    ('Rautahat', 'Rautahat'),
    ('Rolpa', 'Rolpa'),
    ('Rukum', 'Rukum'),
    ('Rupandehi', 'Rupandehi'),
    ('Salyan', 'Salyan'),
    ('Sankhuwasabha', 'Sankhuwasabha'),
    ('Saptari', 'Saptari'),
    ('Sarlahi', 'Sarlahi'),
    ('Sindhuli', 'Sindhuli'),
    ('Sindhupalchok', 'Sindhupalchok'),
    ('Siraha', 'Siraha'),
    ('Solukhumbu', 'Solukhumbu'),
    ('Sunsari', 'Sunsari'),
    ('Surkhet', 'Surkhet'),
    ('Syangja', 'Syangja'),
    ('Tanahu', 'Tanahu'),
    ('Taplejung', 'Taplejung'),
    ('Terhathum', 'Terhathum'),
    ('Udayapur', 'Udayapur'),
]

PROVINCE_NO = [ (1, 1),(2, 2),(3, 3),(4, 4),(5, 5),(6, 6),(7, 7)]

# Create your models here.
class SiteInformation(models.Model):

    Logo=fields.FileField("Logo",  format="Image")
    Site_Title = models.CharField(max_length=100, null=False, blank=False)
    Site_Meta_Key = models.CharField(max_length=160, null=False, blank=False)
    Site_Meta_Description = models.TextField(max_length=160, null=False, blank=False)
    Footer_Logo=fields.FileField("Footer Logo",  format="Image")
    def __str__(self):
        return "Edit Here"

    def __unicode__(self):
        return "Edit Here"

    class Meta:
        verbose_name_plural = 'Site Information'


class AboutUs(models.Model):
    Content=fields.RichTextField(null=True, blank=True)
    def __str__(self):
        return "About Us"

    def __unicode__(self):
        return "About Us"

    class Meta:
        verbose_name_plural = 'About Us'



class Data_template(Page):
    pass

    def __str__(self):
        return  "Projects"

    class Meta:
        verbose_name = 'Data'
        verbose_name_plural = 'Dataset'

class Data(models.Model):
    Data_Title = models.CharField(max_length=100, null=False, blank=False)
    GitHub_Link = models.URLField()
    added = models.DateTimeField(auto_now_add=True)
    type=models.CharField(max_length=100, null=True, blank=True, choices=DATASET_TYPES)
    district=models.CharField(max_length=100, null=True, blank=True,choices=DISTRICT)
    province=models.IntegerField(null=True, blank=True,choices=PROVINCE_NO)

    def __str__(self):
        return  self.Data_Title

    def __unicode__(self):
        return self.Data_Title



class  Visualization_template(Page):
    pass
    def __str__(self):
        return  "Visualization"

    class Meta:
        verbose_name = 'Visualizations'
        verbose_name_plural = 'Visualization'


class Visualization(models.Model):
    Data_Title = models.CharField(max_length=100, null=False, blank=False)
    Inforgraphic =fields.FileField("Viusalization Image",  format="Image")
    GitHub_Link = models.URLField(null=True, blank=True)
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True,)


    def __str__(self):
        return self.Data_Title

    def __unicode__(self):
        return self.Data_Title
