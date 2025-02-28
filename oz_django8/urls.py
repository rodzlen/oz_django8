"""
URL configuration for oz_django8 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path

# from ninja import NinjaAPI

# from tabom.services.like_service import do_like
#
# api = NinjaAPI()
#
#
# @api.get("like")
# def api_do_like(request, user_id: int, article_id: int):
#     do_like(user_id, article_id)
#     return None


urlpatterns = [
    path("admin/", admin.site.urls),
    # path("api/", api.urls),
]
