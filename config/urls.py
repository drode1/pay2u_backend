from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from app.auth_jwt.api.urls import token_urlpatterns
from app.subscriptions.api.urls import subscriptions_urlpatterns
from app.users.api.urls import user_patterns

api_v1_patterns = [
    path('login/', include((token_urlpatterns, 'auth_jwt'))),
    path('clients/', include((user_patterns, 'users'))),
    path('subscriptions/', include((subscriptions_urlpatterns, 'subscriptions')))
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include((api_v1_patterns, ''))),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
