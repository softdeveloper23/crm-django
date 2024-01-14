from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name=""),
    path("register/", views.register, name="register"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("dashboard/", views.dashboard, name="dashboard"), # - CRUD starts here
    path("create-record/", views.create_record, name="create-record"),
    path("update-record/<int:pk>/", views.update_record, name="update-record"),
    path("record/<int:pk>/", views.singular_record, name="record"),
]
