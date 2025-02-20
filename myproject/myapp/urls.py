from django.urls import path

from . import views


app_name = 'myapp'

urlpatterns = [
    path('morning/', views.morning),
    path('number/<int:val>', views.num),
    path('sentence/<str:letter>', views.sentence),
    path('old_url', views.old_url),
    path('new_url', views.new_url),
    path('new', views.new_page_url, name="newreverse"),
    path('old', views.old_page_url, name="oldpage"),
    path('mainindex/', views.index),
    path('detail/<int:blog_id>', views.detail, name='detail'),
]