from django.db import models

# Create your models here.

class City(models.Model):
    class Meta:
        verbose_name_plural = "cities"
        ordering = ['country', 'name']

    name =  models.CharField(max_length=200, unique=True)
    country = models.CharField(max_length=200)
    lat = models.FloatField(null=True, blank=True)
    lng = models.FloatField(null=True, blank=True)

    def __unicode__(self):              # __str__ on Python 3
        return self.name

class Tag(models.Model):
    class Meta:
        ordering = ['name']

    name = models.CharField(max_length=200, unique=True)

    def __unicode__(self):              # __str__ on Python 3
        return self.name

class Service(models.Model):
    service = models.CharField(max_length=200, unique=True)

    def __unicode__(self):              # __str__ on Python 3
        return self.service

class Company(models.Model):
    class Meta:
        verbose_name_plural = "companies"
        ordering = ['name']

    name = models.CharField(max_length=200, unique=True)
    city = models.ForeignKey(City, related_name='headquarters_city')
    branch_cities = models.ManyToManyField(City, null=True, blank=True, related_name='branch_cities')
    description = models.TextField(max_length=2000)
    tags = models.ManyToManyField(Tag)
    url = models.URLField(max_length=200)
    logo_url = models.URLField(max_length=200, null=True, blank=True)
    n_of_employees = models.IntegerField(null=True, blank=True)
    business_id = models.CharField(max_length=200, null=True, blank=True)
    services = models.ManyToManyField(Service)

    def __unicode__(self):              # __str__ on Python 3
        return self.name
