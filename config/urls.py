"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, re_path, include
from rest_framework.routers import DefaultRouter
from accounts.urls import router as accountsRouter
from shop.urls import router as shopRouter

root_router = DefaultRouter()
root_router.registry.extend(accountsRouter.registry)
root_router.registry.extend(shopRouter.registry)

urlpatterns = (
    path('admin/', admin.site.urls),
    path('api/', include(root_router.urls)),
    path('', include('accounts.urls'))
) + tuple(static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += (
        re_path(r'^__debug__/', include(debug_toolbar.urls)),
    )
