from django.urls import path
from .views import IndexPage
# from django.shortcuts import redirect

app_name="home"
urlpatterns=[
    path('', IndexPage.as_view(), name="home" )
]