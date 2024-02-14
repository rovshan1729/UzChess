from django.urls import path
from course import views

urlpatterns = [
    path("", views.CourseListAPIView.as_view()),
    path("/<int:pk>", views.CourseRetriveAPIView.as_view()),
]
