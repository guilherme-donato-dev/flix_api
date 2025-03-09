from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

urlpatterns = [
    path('authentication/token/', TokenObtainPairView.as_view(), name='token-obtain-pair'),
    path('authentication/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), #o refresh ele dura 24 horas e durante a sua duração ele fica gerando novos access tokens, com duração de 5 minutos cada
    path('authentication/token/verify/', TokenVerifyView.as_view(), name='token_verify'), #verify só verifica se o token ainda está válido ou não
]