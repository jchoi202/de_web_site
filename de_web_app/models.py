# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Property(models.Model):
    property_name = models.CharField(max_length=255)
    franchise_series = models.CharField(max_length=255)
    type = models.CharField(max_length=25)
    year = models.IntegerField(null=True)
    franchise_year = models.IntegerField(null=True)
    season = models.IntegerField(null=True)
    season_title = models.CharField(max_length=255, null=True)
    divisions = models.ManyToManyField('Division', through='PropertyDivision')

    def __unicode__(self):
        return self.property_name

class Asset(models.Model):
    asset_id = models.CharField(max_length=100)
    property_name = models.ForeignKey(Property)
    source = models.CharField(max_length=25)

class Division(models.Model):
    division_id = models.AutoField(primary_key=True)
    division_name = models.CharField(max_length=25)

class PropertyDivision(models.Model):
    division_id = models.ForeignKey(Division)
    property_name = models.ForeignKey(Property)