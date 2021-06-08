from rest_framework import routers
from django.urls import path, include
from course import views

router = routers.DefaultRouter()

urlpatterns = [
    path("", include(router.urls)),
    path("list/", views.ListAndCreateCourse.as_view()),
    path("<int:pk>/", views.RetrieveUpdateDestroyCourse.as_view()),
    path("<int:course_id>/modules/", views.ListAndCreateCourseModule.as_view()),
    path("<int:course_id>/modules/<int:pk>/", views.RetrieveUpdateDestroyCourseModule.as_view()),
    path("<int:course_id>/evaluations/", views.ListAndCreateCourseEvaluations.as_view()),
    path("<int:course_id>/evaluations/<int:pk>/", views.RetrieveUpdateDestroyCourseEvaluations.as_view()),
    path("<int:course_id>/students/", views.ListAndCreateCourseStudents.as_view()),
    path("<int:course_id>/students/<int:pk>/", views.RetrieveUpdateDestroyCourseStudents.as_view()),
]