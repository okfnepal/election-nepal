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


class Candidate(models.Model):

    status_choices = (
        ('Approved', 'Approved'),
        ('Pending', 'Pending'),

    )
    Name = models.CharField(max_length=100, null=True, blank=True)
    Party = models.CharField(max_length=100, null=True, blank=True)
    Position = models.CharField(max_length=100, null=True, blank=True)
    Picture = models.ImageField(blank=True)
    Election_Symbol = models.ImageField(blank=True)
    Short_Bio = models.CharField(max_length=100, null=True, blank=True)
    Age = models.IntegerField(null=True, blank=True)
    Education = models.CharField(max_length=100, null=True, blank=True)
    Experience = models.CharField(max_length=500, null=True, blank=True)
    Promises = models.CharField(max_length=500, null=True, blank=True)

    Contributor_Name = models.CharField(max_length=100, null=True, blank=True)
    Contributor_PhoneNumber = models.CharField(max_length=100, null=True, blank=True)

    Status = models.CharField(max_length=225, choices=status_choices, blank=True)

    def picture_inline(self):
        return u'<img width="150" height="150" src="/static/media/%s" />' % self.Picture

    picture_inline.short_description = 'Picture'
    picture_inline.allow_tags = True

    def symbol_inline(self):
        return u'<img width="150" height="150" src="/static/media/%s" />' % self.Election_Symbol

    symbol_inline.short_description = 'Election Symbol'
    symbol_inline.allow_tags = True

    class Meta:
        verbose_name = 'Candidates'
        verbose_name_plural = 'Candidate'

    def __str__(self):
        return self.Name+":"+self.Party

    def __unicode__(self):
        return self.Name+":"+self.Party