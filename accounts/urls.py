from django.contrib.auth.views import LogoutView, PasswordChangeView
from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from accounts.views import home, LoginUser, update, signup
from .views import ProfileViewSet

router = DefaultRouter()
router.register(r'profiles', ProfileViewSet, basename='profile')

urlpatterns = (
    path('token_login/', TokenObtainPairView.as_view(), name='token_obtain'),
    path('token_login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('login/', LoginUser.as_view(), name="login"),
    path('logout/', LogoutView.as_view(next_page="/auth"), name='logout'),
    path('signup/', signup, name='signup'),
    path('update/', update, name='update'),
    path('password/', PasswordChangeView.as_view(template_name='accounts/password.html',
         success_url="/"), name='password'),
    path('', home, name='home'),
)
