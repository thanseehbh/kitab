from django.contrib import admin
from django.urls import path
from myapp import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'myapp'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login_page,name='login'),
    path('home/', views.home_page,name='home'),
    path('register_page/', views.register_page,name='register'),
    path('signup_page/', views.signup_page,name='signup'),
    path('logout_link/', views.logout_link,name='logout'),
    path('profile_page/', views.profile_page,name='profile'),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
