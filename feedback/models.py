from django.conf import settings
from django.db import models
from django.core.validators import RegexValidator
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy as _


# Create your models here.
class Feedback(models.Model):
    url = models.CharField(_('Url'), max_length=255)
    browser = models.TextField(_('Browser'))
    comment = models.TextField(_('Comment'))
    screenshot = models.ImageField(_('Screenshot'), blank=True, null=True, upload_to="static/screenshots/")

    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_("User"), on_delete=models.SET_NULL, blank=True, null=True)
    email = models.EmailField(max_length=254, blank=True, null=True)
    phone_number_regex = RegexValidator(regex='^((\+91|91|0)[\- ]{0,1})?[456789]\d{9}$', message='Please Enter 10/11 digit mobile number or landline as 0<std code><phone number>', code='invalid_mobile')
    phone = models.CharField(max_length=14,verbose_name='Phone - ഫോണ്‍ നമ്പര്‍', validators=[phone_number_regex])
    created = models.DateTimeField(_('Creation date'), auto_now_add=True)


    def screenshot_thumb(self):
        if self.screenshot:
            return mark_safe(u'<img src="%s" width="%s" />' % (self.screenshot.url, "50%"))
        else:
            return 'No Image Found'
    screenshot_thumb.allow_tags = True
    screenshot_thumb.short_description = _("Screenshot")
