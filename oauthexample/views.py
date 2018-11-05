import logging

from rest_framework import (
    schemas,
    response,
    permissions,
    viewsets,
    mixins,
)
from django.http import JsonResponse
from django.conf import settings
from django.views.generic import View
from rest_framework.decorators import (
    api_view,
    permission_classes,
    renderer_classes,
    detail_route,
)
from rest_framework_swagger.renderers import OpenAPIRenderer
from rest_framework_swagger.renderers import SwaggerUIRenderer


logger = logging.getLogger(__name__)

class CIPAPIOpenAPIRenderer(OpenAPIRenderer):
    def get_customizations(self):
        data = super(CIPAPIOpenAPIRenderer, self).get_customizations()
        scheme = 'https' if settings.CIPAPI_SWAGGER_FORCE_HTTPS else 'http'
        data['scheme'] = scheme
        data['schemes'] = [scheme, ]
        return data


@api_view()
@renderer_classes([CIPAPIOpenAPIRenderer, SwaggerUIRenderer])
@permission_classes((permissions.AllowAny,))
def schema_view(request):
    from oauthexample.urls import urlpatterns
    generator = schemas.SchemaGenerator(
        title='Example auth app',
        patterns=urlpatterns
    )
    return response.Response(generator.get_schema(request=request))


class HelloWorld(View):
    def get(self, request, *args, **kwargs):
        return JsonResponse({"Hello": "World"})
