from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from rest_framework.views import APIView
import logging, traceback
logging.basicConfig(filename="./logs/iris.log", level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(name)s:%(message)s')

# logger = logging.getLogger(__name__)
# logger.setLevel(logging.INFO)
#
# formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s')
#
# file_handler = logging.FileHandler("./logs/iris.log")
# file_handler.setFormatter(formatter)
#
# logger.addHandler(file_handler)


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


            logging.info('Created iris: {} , {} , {} , {}'.format('sepal_length: ' + request_sl,  'sepal_width: '+ request_sw, 'petal_length: ' + request_pl, 'petal_width: '+ request_pw))

            data = [request_sl, request_sw, request_pl, request_pw]
            data = np.array(data).reshape(-1, 4)
            result = IrisAppConfig.model.predict(data)

            predict_flower = ['Setosa', 'versicolor', 'virginica']
            result = predict_flower[result[0]]

            logging.info('Predicted Flower: {}'.format(result))

            context = {"result": result}
            return JsonResponse(context)
        return render(request, "index.html")

