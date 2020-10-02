from django.urls import path
from .views import MovieView, MovieDetailView

urlpatterns = [
    path('', MovieView.as_view()),
    path('<int:pk>/', MovieDetailView.as_view())
]
