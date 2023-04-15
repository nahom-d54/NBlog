from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='home'),
    path('<int:pk>/', views.post_detail, name='post_detail'),
    path('create/',views.create_post,name='create_post')
]