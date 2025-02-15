from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('login/',views.login_user,name='login'),
    # We have created logout url but not a page because we want a redirect it to home.
    path('logout/',views.logout_user,name='logout'),
    path('register/',views.register_user,name='register'),
]