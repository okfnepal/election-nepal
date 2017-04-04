from __future__ import unicode_literals
from  mezzanine.core import  fields
from mezzanine.pages.models import Page

from django.db import models

# Create your models here.
class SiteInformation(models.Model):
    Logo=fields.FileField("Logo",  format="Image")
    Site_Title = models.CharField(max_length=100, null=False, blank=False)
    Site_Meta_Key = models.CharField(max_length=160, null=False, blank=False)
    Site_Meta_Description = models.TextField(max_length=160, null=False, blank=False)
    Footer_Logo=fields.FileField("Footer Logo",  format="Image")
    def __str__(self):
        return "Edit Here"

    class Meta:
        verbose_name_plural = 'Site Information'

class AboutUs(models.Model):
    Content=fields.RichTextField()
    def __str__(self):
        return "About Us"

    class Meta:
        verbose_name_plural = 'About Us'



class Data_template(Page):
    content=fields.RichTextField()

    def __str__(self):
        return  "Projects"

    class Meta:
        verbose_name = 'Data'
        verbose_name_plural = 'Datas'

class Data(models.Model):
    Data_Title = models.CharField(max_length=100, null=False, blank=False)
    Dataset=fields.FileField("Dataset")
    GitHub_Link = models.URLField()
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return  self.Data_Title



class  Visualization_template(Page):
    content = fields.RichTextField()
    def __str__(self):
        return  "Visualization"

    class Meta:
        verbose_name = 'Visualization'
        verbose_name_plural = 'Visualizations'

class Visualization(models.Model):
    Data_Title = models.CharField(max_length=100, null=False, blank=False)
    Inforgraphic =fields.FileField("Viusalization Image",  format="Image")
    GitHub_Link = models.URLField()
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Data_Title




