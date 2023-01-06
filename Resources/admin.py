from django.contrib import admin
from .models import *

admin.site.register(department)
admin.site.register(Textbook)
admin.site.register(PastQuestion)
admin.site.register(Material)

