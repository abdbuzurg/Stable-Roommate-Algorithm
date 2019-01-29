from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

urlpatterns = [
    path('', views.HOME, name = 'HOME'),
    path('survey/', views.SURVEY, name='SURVEYS'),
    path('answers/', views.SurveyList, name='answers'),
    path('answers/naryn-male', views.NarynMale, name='naryn-male'),
    path('answers/naryn-female', views.NarynFemale, name='naryn-female'),
    path('answers/khorog-male', views.KhorogMale, name='khorog-male'),
    path('answers/khorog-female', views.KhorogFemale, name='khorog-female'),
    path('answers/tekeli-male', views.TekeliMale, name='tekeli-male'),
    path('answers/tekeli-female', views.TekeliFemale, name='tekeli-female'),
    path('survey/<int:id>/', views.SurveyDetail, name='survey-detail'),
    path('match/<int:campus>/<int:gender>', views.Match, name='match')
    # path("surveys/", views.apiSurveyList, name="survey_list"),
    # path("surveys/<int:pk>/", views.apiSurveyDetail, name="survey_detail"),

]

urlpatterns += staticfiles_urlpatterns()
