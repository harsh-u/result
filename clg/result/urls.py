from django.urls import path
from . import views
urlpatterns = [
    path("", views.index, name="result"),
    path("<int:student_id>", views.student_results, name='student_results')
    ]