from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name='apiOverview'),
    path('openai/', views.openai_api, name='openai_api'),

]
