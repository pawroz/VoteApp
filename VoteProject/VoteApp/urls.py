from django.urls import path

from django.contrib.auth import views as auth_views

from . import views

#app_name = 'VoteApp'

urlpatterns = [
    path('', views.home, name='home'),
    path('charts', views.index, name='index'),

    path('register', views.registerPage, name='registerPage'),
    path('login', views.loginPage, name='loginPage'),
    path('logout/', views.logoutUser, name='logout'),

    path('detail/<str:pk>', views.detail, name='detail'),
    path('results/<str:pk>', views.results, name='results'),
    path('resultsData/<str:pk>', views.resultsData, name='resultsData'),

    path('addPolling', views.addPolling, name='addPolling'),
    path('vote/<str:pk>', views.vote, name='vote'),

    path('reset_password/',
        auth_views.PasswordResetView.as_view(template_name='../templates/VoteApp/password_reset.html'),
        name="reset_password"),
    path('reset_password_sent/', 
        auth_views.PasswordResetDoneView.as_view(template_name='../templates/VoteApp/password_reset_sent.html'), 
        name="password_reset_done"),
    path('reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(template_name='../templates/VoteApp/password_reset_form.html'), 
        name="password_reset_confirm"),
    path('reset_password_complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name='../templates/VoteApp/password_reset_done.html'), 
        name="password_reset_complete"),
]
