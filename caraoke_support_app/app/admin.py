from django.contrib import admin
from .models import Singer
from .models import Song

admin.site.register(Singer)
admin.site.register(Song)
# Register your models here.
