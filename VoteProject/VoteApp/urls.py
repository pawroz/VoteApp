from django.urls import path

from . import views

app_name = 'VoteApp'

urlpatterns = [
    path('', views.home, name='home'),
    path('charts', views.index, name='index'),

    path('registerPage', views.registerPage, name='registerPage'),
    path('loginPage', views.loginPage, name='loginPage'),

    path('detail/<str:pk>', views.detail, name='detail'),
    path('results/<str:pk>', views.results, name='results'),
    path('resultsData/<str:pk>', views.resultsData, name='resultsData'),

    path('vote/<str:pk>', views.vote, name='vote'),


]
