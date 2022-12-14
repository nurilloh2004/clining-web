"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.conf.urls.i18n import i18n_patterns
# from django.contrib import admin
# from django.urls import path, include
# from django.conf import settings
# from django.conf.urls import handler404
# from django.conf.urls.static import static
# from django.utils.translation import gettext_lazy as _

# urlpatterns = [
#     path("i18n/", include("django.conf.urls.i18n")),
#     path('', include('clining.urls')),
#     path('rosetta/', include('rosetta.urls')),

# ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# urlpatterns += i18n_patterns(path("admin/", admin.site.urls))
# urlpatterns += i18n_patterns(path("", include('clining.urls')))
# urlpatterns += i18n_patterns(path('rosetta/', include('rosetta.urls')))

from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path, include
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from django.conf.urls import handler404
from django.conf.urls.static import static


urlpatterns = i18n_patterns(
    path(_('admin/'), admin.site.urls),
    path('rosetta/', include('rosetta.urls')),
    path('', include('clining.urls')),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)