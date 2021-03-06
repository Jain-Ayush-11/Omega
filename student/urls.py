from django.urls import path, re_path
from . import views

urlpatterns = [
    path('create/', views.StudentCreateView.as_view()),
    path('profile/', views.StudentDetailView.as_view()),
    path('series/', views.SeriesView.as_view()),
    path('educator-list/', views.EducatorsView.as_view()),
    path('educator-profile/<int:pk>/', views.EducatorDetailsView.as_view()),
    path('wishlist/', views.WishlistView.as_view()),
    path('notification/', views.NotificationView.as_view()),
    path('notification/read/<int:pk>/', views.ReadNotificationView.as_view()),
    path('story-users/', views.StoryUserView.as_view()),
    path('story/<int:pk>/', views.StoryView.as_view()),
    path('quiz/', views.QuizView.as_view()),
    path('quiz/question/attempt/', views.AttemptView.as_view()),
    path('quiz/<int:pk>/analysis/', views.AttemptedQuestionsView.as_view()),
    path('quiz/score/<int:pk>/', views.ScoreView.as_view()),
    path('search/profile/<str:username>/', views.ProfileSearchView.as_view()),
    path('search/series/<str:name>/', views.SeriesSearchView.as_view()),
]
