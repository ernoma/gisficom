from django.contrib import admin
from django.forms import Textarea
from django.db import models

# Register your models here.

from .models import Company, City, Tag, Service

class TagInline(admin.TabularInline):
    model = Company.tags.through
    extra = 3

class CompanyAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name', 'description', 'business_id']}),
        ('Locations', {'fields': ['city', 'branch_cities']}),
        ('Misc', {'fields': ['url', 'logo_url', 'n_of_employees']}),
    ]
    inlines = [TagInline]
    list_display = ('name', 'city', 'get_branch_cities', 'n_of_employees')

    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 4, 'colls': 20})},
    }

    def get_branch_cities(self, obj):
        return "\n".join([c.name for c in obj.branch_cities.all()])
    get_branch_cities.short_description = "branch cities"
    

admin.site.register(Company, CompanyAdmin)

admin.site.register(City)

admin.site.register(Tag)

admin.site.register(Service)
