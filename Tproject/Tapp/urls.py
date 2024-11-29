from django.urls import path

from.import views
urlpatterns=[
    path('',views.gov),
    path('bio',views.bio),
]