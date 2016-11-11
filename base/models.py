from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __unicode__(self):
        return u'%s' % (self.user, )


class ProfileSetting(models.Model):
    profile = models.ForeignKey('base.Profile', null=False)
    setting = models.ForeignKey('base.Setting', null=False)

    # TODO: Need to make this an encrypted field
    value = models.CharField(max_length=2048)

    def __unicode__(self):
        return u'%s: %s' % (self.setting, self.profile)


class Setting(models.Model):
    name = models.CharField(max_length=512, blank=False)

    def __unicode__(self):
        return u'%s' % (self.name, )
