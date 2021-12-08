from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from rest_framework.views import APIView
from . import forms
from iris_app import views
from .apps  import IrisAppConfig
# Create your views here.

class irisAPIView(APIView):
    def __init__(self):
        pass

    def post(self, request, format=None):
        request_sl = request.data["sl"]
        request_sw = request.data["sw"]
        request_pl = request.data["pl"]
        request_pw: object = request.data["pw"]
        prediction = DjangoappConfig.model.predict()

        if prediction == 0:
            flower = "setosa"
        elif prediction == 1:
            flower = "versicolor"
        else : flower = "virginica"

        out = dict(name=request_sl, flower=flower)
        return JsonResponse(out)