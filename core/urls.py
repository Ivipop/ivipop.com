
from django.urls import path
from evenement import views
urlpatterns = [
    path('', views.IndexGet ),
    path('<str:lang>/', views.IndexGet ),
    path('r', views.RechercheGet ),
    path('<str:lang>/r', views.RechercheGet ),
    path('<str:slug>', views.MentionsGet ),
    path('<str:lang>/<str:slug>', views.MentionsGet ),
]
