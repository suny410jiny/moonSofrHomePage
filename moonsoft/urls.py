from re import template

from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('baseApp/', include('baseApp.urls')),
    path('', RedirectView.as_view(pattern_name='baseApp:index'), name='root'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]+ static (settings.STATIC_URL, document_root = settings.STATIC_ROOT)



if settings.DEBUG:
    print(settings.DEBUG)
    import debug_toolbar
    urlpatterns +=[
        path('__debug__/', include(debug_toolbar.urls)),
    ]
    urlpatterns += static(settings.MEDIA_URL,
                   document_root=settings.MEDIA_ROOT)