import json
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt


from .api import JotformDataAPI


class JotformView(View):
    def get(self, request):
        jotform_data_api = JotformDataAPI()
        # result_get_user = jotform_data_api.get_user()
        # result_get_all_form = jotform_data_api.get_all_form()
        result_submmission = jotform_data_api.get_submission_data_from_form()

        print(result_submmission)
        html = 'test api look at console'
        return HttpResponse(html)

class WebhookView(View):
    def post(self, request):
        print(request.POST)
        return HttpResponse()

    def get(self, request):
        html='this is webhook'
        return HttpResponse(html)

