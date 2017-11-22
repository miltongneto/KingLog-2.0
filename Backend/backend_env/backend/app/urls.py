"""
	URLs do app
"""

from django.conf.urls import url, include
from rest_framework import routers
from .views import ClienteService

router = routers.SimpleRouter()
router.register('clientes', ClienteService, 'cliente')

urlpatterns = [
		url(r'^', include(router.urls))
	]