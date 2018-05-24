from django.urls import path
from . import views

urlpatterns = [
    #/polls/
    path('', views.index, name='index'),
    #/polls/[Integer]/
    path('<int:question_id>/', views.detail, name='detail'),
    #/polls/[Integer]/results/
    path('<int:question_id>/results/', views.results, name='results'),
    #/polls/[Integer]/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
