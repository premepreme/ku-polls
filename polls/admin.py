from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Question, Choice, Vote

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Vote)