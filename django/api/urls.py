from django.conf.urls import include, url
from django.views.generic import RedirectView, TemplateView

from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token

from . import views

router = routers.DefaultRouter()
router.register(r'items', views.ItemViewSet)

urlpatterns = [
    url(r'^v1/', include(router.urls, namespace='v1')),
    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^auth/token/', obtain_jwt_token),
    url(r'^$', RedirectView.as_view(url='/api/v1/')),
]
