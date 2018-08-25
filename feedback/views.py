import json
from base64 import b64decode

from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
from django.core.files.base import ContentFile
from django.utils.crypto import get_random_string
from django.views.generic import View

from mainapp.redis_queue import sms_queue
from mainapp.sms_handler import send_confirmation_sms
from .forms import FeedbackForm


class FeedBackView(View):
    def post(self, request):
        if request.method == 'POST' and request.is_ajax():

            feedback = json.loads(request.POST["feedback"])
            data = {'url': feedback['url'], 'browser': json.dumps(feedback['browser']), 'comment': feedback['note'],
                    'phone': feedback.get('phone')}
            if request.user.id:
                data['user'] = request.user.id
            imgstr = feedback['img'].split(';base64,')[1]
            file = {'screenshot': ContentFile(b64decode(imgstr), name="screenshot_" + get_random_string(6) + ".png")}
            form = FeedbackForm(data, file)

            # check whether it's valid and send sms confirmation:
            if form.is_valid():
                f = form.save()
                sms_queue.enqueue(
                    send_confirmation_sms, f.phone
                )
                return HttpResponse(status=200)
            else:
                return JsonResponse({'error': dict(form.errors)})

        else:
            return HttpResponseBadRequest()
