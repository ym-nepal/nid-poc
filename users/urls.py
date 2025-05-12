from django.urls import path, include
from rest_framework.routers import DefaultRouter
from users.views import UserViewSet
from nid.views import NIDViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register('users', UserViewSet, basename='user')
router.register('nids', NIDViewSet, basename='nid')

urlpatterns = [
    path('', include(router.urls)),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
