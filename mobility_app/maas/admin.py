from maas.models import Category
from django.contrib import admin
from .models import Attribute, Category

class AttributeInline(admin.TabularInline):
    model = Attribute

class CategoryAdmin(admin.ModelAdmin):
    inlines = [AttributeInline,]
# Register your models here.
admin.site.register(Category,CategoryAdmin)