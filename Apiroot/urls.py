"""Apiroot URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.schemas import get_schema_view
from django.views.generic import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('SerializertionApi.urls')),
    path('create/', include('DeSerializationApi.urls')),
    path('crud/', include('basicCRUDApi.urls')),
    path('val/', include('ValidationApi.urls')),
    path('models/', include('modelsSerializerApi.urls')),
    path('func/', include('FunctionBasedViewAPi.urls')),
    path('cls/', include('ClassBasedViewAPi.urls')),
    path('gen/', include('GenericViewApi.urls')),
    path('cv/', include('ConcreteViewApi.urls')),
    path('vs/', include('ViewSetApi.urls')),

    # docs
    path('api_schema', get_schema_view(title='api schema',
                                       description='guide'), name='api_schema'),
    path('', TemplateView.as_view(
        template_name='docs.html',
        extra_context={'schema_url': 'api_schema'}
    ), name='swagger-ui'),
]
