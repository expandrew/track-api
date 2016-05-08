from django.conf.urls import include, url
from django.views.generic import RedirectView, TemplateView

from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'items', views.ItemViewSet)

urlpatterns = [
    url(r'^v1/', include(router.urls, namespace='v1')),
    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^$', RedirectView.as_view(url='/api/v1/')),
]
