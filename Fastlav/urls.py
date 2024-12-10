from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from usuario import views

router = routers.SimpleRouter()
router.register('apisesion', views.viewsAPi.as_view({"post":"create"}), basename="apisesion")
urlpatterns = [
    path('admin/', admin.site.urls),
    path('apisesion/', views.viewsAPi.as_view({"post":"create"})),

]
