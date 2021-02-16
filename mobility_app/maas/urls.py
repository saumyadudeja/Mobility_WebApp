from django.urls import path,include
from . import views
from .views import UseCaseClass

urlpatterns = [
    
    #path('technology/<int:pk>/', views.Technology.as_view() , name='technology'),
    path('',views.home,name='home'),
    # UseCaseClass.as_view(),name='home'),
    #path('accounts/',include("allauth.urls")),
    path('technology/',views.technology,name='newtechnology'),
    path('register/',views.registerPage,name='register'),
    path('login/',views.loginPage,name='login'),
    path('logout/',views.logoutUser,name='logout'),

]