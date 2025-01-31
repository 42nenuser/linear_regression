from django.urls import path
from django.views.generic import TemplateView
from .views import predict_price

urlpatterns = [
    path('predict/', predict_price, name='predict_price'),
    path('', TemplateView.as_view(template_name="index.html"), name="home"),  # Serve frontend
]
