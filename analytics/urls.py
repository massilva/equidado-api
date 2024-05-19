from django.urls import path

from analytics.views import CustomAuthToken

urlpatterns = [
    path('token-auth/', CustomAuthToken.as_view(), name='token_auth'),
]
