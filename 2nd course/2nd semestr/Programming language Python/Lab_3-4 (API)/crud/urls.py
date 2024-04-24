from django.urls import path
from .user.viewsets import UpdateUserApiView, CreateUserApiView
from .record.viewsets import UpdateRecordApiView, CreateRecordApiView



urlpatterns = [
    path('users/<int:id>/', UpdateUserApiView.as_view()),
    path('users/', CreateUserApiView.as_view()),
    path('records/<int:id>/', UpdateRecordApiView.as_view()),
    path('records/', CreateRecordApiView.as_view()),
]