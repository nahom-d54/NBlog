
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from .globals import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',lambda request: redirect('home'),name='index'),
    path('blog/',include('blog.urls'),name='posts'),
    path('accounts/login/',views._login,name='sign_in'),
    path('accounts/sign_up/',views.sign_up,name='sign_up'),
    path('accounts/logout/',views._logout,name='logout')
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
