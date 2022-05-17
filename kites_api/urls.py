from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView, TokenVerifyView,
)
from django_ses.views import DashboardView, SESEventWebhookView
from django.views.decorators.csrf import csrf_exempt
from users.views import CustomAuthToken

schema_view = get_schema_view(
    openapi.Info(
        title="Kites Api",
        default_version='v1',
        description="Kites Foundation",
        terms_of_service="https://kitesfoundation.org",
        contact=openapi.Contact(email="hey@syam.dev"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


class CustomSESDashboardView(DashboardView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(**admin.site.each_context(self.request))
        return context


urlpatterns = [
                  re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0),
                          name='schema-json'),
                  re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
                  re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
                  re_path(r'^ses/event-webhook/$', SESEventWebhookView.as_view(), name='handle-event-webhook'),
                  path('admin/', admin.site.urls),
                  path('user/', include('users.urls')),
                  path('api-auth/', include('rest_framework.urls')),
                  path('auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
                  path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
                  path('auth/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
                  path("health/", include("healthy_django.urls", namespace="healthy_django")),
                  re_path(r'^admin/django-ses/', CustomSESDashboardView.as_view(), name='django_ses_stats'),
                  path('api-token-auth/', CustomAuthToken.as_view())
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
