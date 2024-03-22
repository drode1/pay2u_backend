from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from app.scores.api.urls import score_patterns

api_v1_patterns = [
    # TODO Здесь список роутов + указание на приложения
    path('users/', include((user_patterns, 'users'))),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    # Здесь просто версионность
    path('api/v1/', include((api_v1_patterns, ''))),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
