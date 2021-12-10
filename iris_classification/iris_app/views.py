from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from rest_framework.views import APIView
from . import forms
from iris_app import views
import numpy as np
from .apps  import IrisAppConfig
# Create your views here.

class irisAPIView(APIView):
    def __init__(self):
        pass

    def post(self, request, format=None):
        if request.method == "POST":
            request_sl = self.request.POST["sl"]
            request_sw = self.request.POST["sw"]
            request_pl = self.request.POST["pl"]
            request_pw = self.request.POST["pw"]

            data = [request_sl, request_sw, request_pl, request_pw]
            data = np.array(data).reshape(-1, 4)
            result = IrisAppConfig.model.predict(data)

            predict_flower = ['Setosa', 'versicolor', 'virginica']
            result = predict_flower[result[0]]

            context = {"result": result}
            return JsonResponse(context)
        return render(request, "index.html")