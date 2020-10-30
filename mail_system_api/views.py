import json

from django.http import JsonResponse, HttpResponse
from rest_framework import views
from rest_framework.response import Response

import requests

from accounts_api import models


class MailSystemAPIView(views.APIView):
    """ 리스트안에 유저들에게 메일 보내기, 메일 수신함확인 """

    def get(self, request):
        """ 메일함 확인 """

        headers = {'Authorization': 'herren-recruit-python'}
        email = request.data.get('email')
        param = {'email': email}
        mail_box = requests.get(
            'http://python.recruit.herrencorp.com/api/v1/inbox/' + str(email),
            headers=headers,
            params=param
        ).text

        return Response(json.dumps(mail_box))

    def post(self, request):
        """ 메일 보내기 """

        headers = {
            'Authorization': 'herren-recruit-python',
            'Content-Type': 'application/x-www-form-urlencoded',
        }

        mailto = request.data['mailto']
        subject = request.data['subject']
        content = request.data['content']
        try:
            models.UserMailList.objects.get(added_email=mailto)

            data = {'mailto': mailto, 'subject': subject, 'content': content}

            mail_send = NoRebuildAuthSession()

            mail_send.post('http://python.recruit.herrencorp.com/api/v1/mail', headers=headers, data=data)

            response = mail_send.post('http://python.recruit.herrencorp.com/api/v1/mail', headers=headers, data=data)

            print(response.status_code)
            return JsonResponse({'status': 'success'}, status=200)

        except:
            return HttpResponse(status=204)


class NoRebuildAuthSession(requests.Session):
    def rebuild_auth(self, prepared_request, response):
        """
        No code here means requests will always preserve the Authorization
        header when redirected.
        Be careful not to leak your credentials to untrusted hosts!
        """
