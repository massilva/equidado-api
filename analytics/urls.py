from django.urls import path

from .views import CustomAuthToken, FeedbackCreateView

urlpatterns = [
    path('token-auth/', CustomAuthToken.as_view(), name='token_auth'),
    path('feedback/', FeedbackCreateView.as_view(), name='feedback-save'),
]
