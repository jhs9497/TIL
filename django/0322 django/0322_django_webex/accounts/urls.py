from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    # Login
    path('login/', views.login, name='login'),

    # Logout
    path('logout/', views.logout, name='logout'),

    # Signup
    path('signup/', views.signup, name='signup'),

    # Delete
    path('delete/', views.delete, name='delete'),
]
