"""seafly URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns

from pages import views

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
    path('admin/', admin.site.urls),
]

urlpatterns += i18n_patterns(
    path('faq', views.getPages),
    path('specification', views.getPages),
    path('contact', views.getContact),
    path('promos', views.getPages),
    path('search', views.search),
    path('convert', views.getPages),
    path('devis', views.getDevis),
    path('incoterms', views.getPages),
    path('promos/<str:pagename>', views.getPageDB),
    path('faq/<str:pagename>', views.getPageDB),
    path('', views.getPages, name='index'),
    path('<str:pagename>', views.getPageDB),
    path('pages/', include('pages.urls')),
)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls))

    ] + urlpatterns
