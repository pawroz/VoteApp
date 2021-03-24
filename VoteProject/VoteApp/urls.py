from django.urls import path

from . import views

app_name = 'VoteApp'

urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<str:pk>', views.detail, name='detail'),
    path('results/<str:pk>', views.results, name='results'),
    path('vote/<str:pk>', views.vote, name='vote'),
    path('resultsData/<str:pk>', views.resultsData, name='resultsData'),

]
