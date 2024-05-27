from django.contrib import admin

from .models import Quiestion, Choice


class ChoiceInline(admin.TabularInline):
    model = Choice


@admin.register(Quiestion)
class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]