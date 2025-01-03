from django.urls import path

from . import views

urlpatterns = [
    path("", views.users_index, name="UsersIndex"),
    path("<int:user_id>/", views.profile_view, name="UserDetail"),
]
