from django.urls import path
from eportal import views

app_name = 'eportal'

urlpatterns = [
    path('ocr/',views.ocr_page,name="ocr_page"),
    path('ocr_output/',views.ocr_output,name="ocr_output"),
]
