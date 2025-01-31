from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('predictor.urls')),  # Include API routes
    path('', TemplateView.as_view(template_name="predictor/index.html"), name="home"),

]
