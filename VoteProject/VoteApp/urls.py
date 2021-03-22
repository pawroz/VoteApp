from django.urls import path

from . import views

app_name = 'VoteApp'

urlpatterns = [
	path('', views.index, name='index'),
	path('detail/<str:pk>', views.detail, name='detail'),
	path('results/<str:pk>', views.index, name='results')
]