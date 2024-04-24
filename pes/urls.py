from django.urls import path
from .views import RegisterCreateAPIView, RegisterRetrieveUpdateDestroyAPIView, LoginAPIView

urlpatterns = [
    path('register/', RegisterCreateAPIView.as_view(), name='register-create'),
    path('register/<int:pk>/', RegisterRetrieveUpdateDestroyAPIView.as_view(), name='register-detail'),
    path('login/', LoginAPIView.as_view(), name='login'),
]


