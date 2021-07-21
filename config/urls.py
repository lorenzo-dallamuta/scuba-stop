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
from django.urls import path, re_path, include
from django.contrib import admin
from django.contrib.auth.views import LogoutView, PasswordChangeView
from django.conf import settings
from django.conf.urls.static import static
from accounts.views import LoginUser, home, signup, update


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', LoginUser.as_view(), name="login"),
    path('logout/', LogoutView.as_view(next_page="/"), name='logout'),
    path('signup/', signup, name='signup'),
    path('update/', update, name='update'),
    path('password/', PasswordChangeView.as_view(template_name='accounts/password.html',
         success_url="/"), name='password'),
    path('api/', include('shop.urls')),
    path('api/profiles/', include('accounts.urls')),
    path('', home, name='home'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        re_path(r'^__debug__/', include(debug_toolbar.urls)),
    ]
