import json
from base64 import b64decode

from django.conf import settings
from django.core.mail import send_mail
from django.utils.translation import ugettext_lazy as _
from django.http import JsonResponse, HttpResponseBadRequest
from django.core.files.base import ContentFile
from django.utils.crypto import get_random_string
from django.shortcuts import reverse
from django.views.generic import View

from .forms import FeedbackForm


class FeedBackView(View):
    def post(self, request):
        if request.method == 'POST' and request.is_ajax():

            # Copy Post data names into names used into the model in order to automatically create the model/form
            # from the request dicts
            feedback = json.loads(request.POST["feedback"])
            if request.user.id:
                data = {'url': feedback['url'], 'browser': json.dumps(feedback['browser']), 'comment': feedback['note'],
                            'user': request.user.id}
            else:
                data = {'url': feedback['url'], 'browser': json.dumps(feedback['browser']), 'comment': feedback['note'],
                            'email': feedback.get('email')}
            imgstr = feedback['img'].split(';base64,')[1]
            file = {'screenshot': ContentFile(b64decode(imgstr), name="screenshot_" + get_random_string(6) + ".png")}
            form = FeedbackForm(data, file)

            # check whether it's valid:
            if form.is_valid():
                f = form.save()

                if hasattr(settings, 'FEEDBACK_EMAIL'):
                    self.send_mail(request, f)
                return JsonResponse({})
            else:
                return JsonResponse({'error': dict(form.errors)})

        else:
            return HttpResponseBadRequest()
    def send_mail(self, request, feedback, fail_silently=False):
        message = _("Your site %(host)s received feedback from %(user)s.\n"
                    "The comments were:\n"
                    "%(note)s.\n\n"
                    "See the full feedback content here: %(url)s") \
                  % {'host': request.get_host(), 'user': str(request.user), 'note': feedback.comment,
                     'url': request.build_absolute_uri(
                         reverse('admin:feedback_feedback_change', args=(feedback.id,)))}
        send_mail(
            _('[%(host)s] Received feedback') % {'host': request.get_host()},
            message,
            settings.ADMIN_EMAIL,
            [settings.FEEDBACK_EMAIL],
            fail_silently=fail_silently)
