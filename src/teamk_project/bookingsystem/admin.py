from django.contrib import admin
from bookingsystem.models import Address, Block, BtmRank, Client, Experiencelevel, Extras, Medicalcondition, Notes, Payment, Paymenttype, Session, Subvenue, SubvenueUsedforSession, UserSelectsSession, Venue

admin.site.register(Address)
admin.site.register(Block)
admin.site.register(BtmRank)
admin.site.register(Client)
admin.site.register(Experiencelevel)
admin.site.register(Extras)
admin.site.register(Medicalcondition)
admin.site.register(Notes)
admin.site.register(Payment)
admin.site.register(Paymenttype)
admin.site.register(Session)
admin.site.register(Subvenue)
admin.site.register(SubvenueUsedforSession)
admin.site.register(UserSelectsSession)
admin.site.register(Venue)
