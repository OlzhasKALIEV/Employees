from django.urls import path

from . import views

urlpatterns = [
    path("employees/", views.EmployeesAPIView.as_view(), name="get_post_employees"),
    path("employees/<int:pk>/", views.EmployeesAPIView.as_view(), name="crud_title"),
    path("departments/", views.DepartmentsAPIView.as_view(), name="get_post_departments"),
    path("departments/<int:pk>/", views.DepartmentsAPIView.as_view(), name="get_post_departments"),
]
