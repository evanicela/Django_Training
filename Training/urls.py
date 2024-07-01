from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("contact/", views.contact, name="contacts"),
    path("about-us/", views.about, name="about"),


    path('service/', views.service_list, name='service_list'),

    # path("courses/", views.courses, name="courses"),
    # path("get-subjects/", views.get_subjects, name="get_subjects"),
    # path("login/", views.login, name="login"),
    # path("register/", views.register, name="register"),
    # path("logout/", views.logout, name="logout"),

]