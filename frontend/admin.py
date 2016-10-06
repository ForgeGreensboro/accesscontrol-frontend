from django.contrib import admin
from frontend import models
from reversion.admin import VersionAdmin

class MachineReservationInline(admin.TabularInline):
    model = models.Reservation
    fields = ['member', 'reservationStart', 'reservationEnd']


class MemberReservationInline(admin.TabularInline):
    model = models.Reservation
    fields = ['machine', 'reservationStart', 'reservationEnd']
    max_num = 0
    extra = 0
    min_num = 0

class MemberSignOffInline(admin.TabularInline):
    model = models.SignOff
    fk_name = 'member'
    readonly_fields = ['signoffDate', 'signoffType', 'machine', 'signOffBy']
    can_delete = False

    def has_add_permission(self, request):
        return False

class MachineAdmin( VersionAdmin):
    fields = ['name', 'macAddress', 'requiresSignOff', 'shop']
    inlines = [MachineReservationInline]


class MembershipAdmin(VersionAdmin):
    fields = ['user']
    inlines = [MemberReservationInline, MemberSignOffInline]


admin.site.register(models.Machine, MachineAdmin)
admin.site.register(models.Membership, MembershipAdmin)
admin.site.register(models.Reservation)
admin.site.register(models.SignOff)
admin.site.register(models.Shop)
