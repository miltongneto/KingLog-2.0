"""
	URLs do app
"""

from django.conf.urls import url, include
from rest_framework import routers
from appBD.views import ClienteCadastroViewSet

router = routers.SimpleRouter()
router.register('clientes', ClienteCadastroViewSet, 'cliente')

urlpatterns = [
		url(r'^', include(router.urls))
	]