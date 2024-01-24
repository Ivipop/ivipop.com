
from django.urls import path
from evenement import views
urlpatterns = [
    path('', views.IndexGet ),
    path('<str:lang>/', views.IndexGet ),
    path('r', views.RechercheGet ),
    path('<str:lang>/r', views.RechercheGet ),
    path('c/c', views.AjoutView.as_view() ),
    path('<str:lang>/c/c', views.AjoutView.as_view() ),
    path('c/o', views.AjoutOptionView.as_view() ),
    path('<str:lang>/c/o', views.AjoutOptionView.as_view() ),
    path('c/i', views.AjoutReponseGet ),
    path('<str:lang>/c/i', views.AjoutReponseGet ),
    path('<str:slug>', views.MentionsGet ),
    path('<str:lang>/<str:slug>', views.MentionsGet ),
]
