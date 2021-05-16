from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from APPS.contacts.models import (Country, State, Currency,
                    Company, Bank, PartnerBank,
                    PartnerCategory, PartnerTitle, Partner,
                    Lang, Users, CountryGroup, PartnerIndustry)

class UsersAdminInline(admin.StackedInline):
    model = Users
    can_delete = False
    verbose_name_plural = 'User'
class UserAdmin(BaseUserAdmin):
    inlines = (UsersAdminInline,)

admin.site.unregister(User)
admin.site.register(Country)
admin.site.register(State)
admin.site.register(Currency)
admin.site.register(Company)
admin.site.register(Bank)
admin.site.register(PartnerBank)
admin.site.register(PartnerCategory)
admin.site.register(PartnerTitle)
admin.site.register(Partner)
admin.site.register(Lang)
admin.site.register(User, UserAdmin)
admin.site.register(CountryGroup)
admin.site.register(PartnerIndustry)