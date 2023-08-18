from django.contrib import admin

from boat.models import Owner, Boat, BoatHistory
from order.models import Order


# Register your models here.


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Boat)
class BoatAdmin(admin.ModelAdmin):
    list_display = ('name', 'year', 'owner', 'price',)
    list_filter = ('year', 'owner',)


@admin.register(BoatHistory)
class BoatHistoryAdmin(admin.ModelAdmin):
    list_display = ('boat', 'start_year', 'stop_year', 'owner',)
    list_filter = ('boat', 'owner',)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('boat', 'email',)
    list_filter = ('boat',)
