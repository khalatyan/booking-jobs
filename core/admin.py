from django.contrib import admin

from core.models import *


class BookingsInline(admin.TabularInline):
    model = Booking
    extra = 0


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name'
    )
    inlines = [BookingsInline]