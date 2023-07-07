from django.contrib import admin

from .models import Gericht, Kategorie

admin.site.register(Gericht)
admin.site.register(Kategorie)