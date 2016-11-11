
from django.contrib import admin

from base.models import Profile, ProfileSetting, Setting


class ProfileAdmin(admin.ModelAdmin):
    pass


class ProfileSettingAdmin(admin.ModelAdmin):
    pass


class SettingAdmin(admin.ModelAdmin):
    pass


admin.site.register(Profile, ProfileAdmin)
admin.site.register(ProfileSetting, ProfileSettingAdmin)
admin.site.register(Setting, SettingAdmin)
