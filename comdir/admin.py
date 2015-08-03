from django.contrib import admin

# Register your models here.

from .models import Company, City, Tag

class TagInline(admin.TabularInline):
    model = Company.tags.through
    extra = 3

class CompanyAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name', 'description']}),
        ('Locations', {'fields': ['city', 'branch_cities']}),
        ('Misc', {'fields': ['url', 'logo_url', 'n_of_employees']}),
    ]
    inlines = [TagInline]
    list_display = ('name', 'city', 'branch_cities', 'n_of_employees')

admin.site.register(Company, CompanyAdmin)

admin.site.register(City)

admin.site.register(Tag)

