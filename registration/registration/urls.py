"""registration URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.SignupPage,name='signup'),
    path('login/',views.LoginPage,name='login'),
    path('home/',views.HomePage,name='home'),
    path('logout/',views.LogoutPage,name='logout'),
    path('submit-request/', views.submit_waste_request, name='submit_waste_request'),
    path('request-status/', views.waste_request_status, name='waste_request_status'),
    path('cancel-request/<int:request_id>/', views.cancel_request, name='cancel_request'),
    path('admin-login/', views.admin_login, name="admin_login"),
    path('admin_dashboard/', views.admin_dashboard, name="admin_dashboard"),
    path('accept-request/<int:request_id>/', views.accept_request, name="accept_request"),
    path('reject-request/<int:request_id>/', views.reject_request, name="reject_request"),
    path("assign_route/<int:request_id>/", views.assign_route, name="assign_route"),
    path('update-route/<int:request_id>/', views.update_route, name='update_route'),
    path('route/', views.route, name="route"),




    
]