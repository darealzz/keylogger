from django.urls import (
    path,
    include
)
from .views import (
    create_session,
    LoggerView
)

urlpatterns = [
    path('test', LoggerView.as_view()),
    path("create/<str:client>", create_session),
]
