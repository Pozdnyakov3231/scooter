from django.urls import path
from . import views

app_name = 'polls'

urlpatterns = [
    path('', views.index, name='index'),  # Список вопросов
    path('<int:question_id>/', views.detail, name='detail'),  # Детали вопроса
    path('<int:question_id>/results/', views.results, name='results'),  # Результаты голосования
    path('<int:question_id>/vote/', views.vote, name='vote'),  # Форма голосования
    path('scooters/', views.scooters_management, name='scooters_management'),  # Управление самокатами
    path('scooters/<int:scooter_id>/change-status/', views.change_scooter_status, name='change_scooter_status'),  # Изменение статуса самоката
]