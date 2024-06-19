from django.urls import path
from dragon_ball import views

urlpatterns = [
    path('', views.indexdb, name='indexdb'),
    path('dragonball_rest/', views.dragonball_rest, name='dragonball_rest'),
    path('users_rest/', views.users_rest, name='users_rest'),
    path('new_dragonball/', views.dragonballView.as_view(), name='new_dragonball'),
    path('new_userdb/', views.NewUserView.as_view(), name='new_user'),
    path('dragonballsaga_rest/', views.dragonballsaga_rest, name='dragonballsaga_rest'),
    path('new_dragonballsaga/', views.dragonballsagaView.as_view(), name='new_dragonballsaga'),
    path('dragonballvivo_rest/', views.dragonballvivo_rest, name='dragonballvivo_rest'),
    path('new_dragonballvivo/', views.dragonballvivoView.as_view(), name='new_dragonballvivo'),
]