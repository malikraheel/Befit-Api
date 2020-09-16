from django.urls import path, include
from .import views

urlpatterns = [
    path('', views.ApiRoot.as_view()),
    path('users/', views.UserList.as_view(), name='users'),
    path('users/<int:pk>/', views.UserDetail.as_view(), name='user'),
    path('profiles/', views.ProfileList.as_view(), name='profiles'),
    path('profiles/<int:pk>/', views.ProfileDetail.as_view(), name='profile'),
    path('messages/', views.MessageList.as_view(), name='messages'),
    path('messages/<int:pk>/', views.MessageDetail.as_view(), name='message'),
    path('exercises/', views.ExerciseList.as_view(), name='exercises'),
    path('exercises/<int:pk>/', views.ExerciseDetail.as_view(), name='exercise'),

]
