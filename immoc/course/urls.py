from django.conf.urls import include, url
from course import views

urlpatterns = [
    url(r'^do/$', views.DoView.as_view()),
]