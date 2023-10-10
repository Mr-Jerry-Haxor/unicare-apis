from django.urls import path
from .views import *

urlpatterns = [
    path('', home),
    path('predict-bupa/', predict_bupa_data , name='predict-bupa-data'),
    path('predict-heart-disease' , predict_heart_disease ,name='predict_heart_disease'),
    path('predict-chronic-kidney-disease' , predict_chronic_kidney_data , name='predict_chronic_kidney_data'),
    path('predict_diabetics' , predict_diabetics_data , name="predict_diabetics_data"),
]
 