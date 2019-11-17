from django.urls import path
from .views import ExpenseView, ExpenseDetailView, CommentListView, TotalView, ActivityListView, ActivityRetrieveView

urlpatterns = [
    path('expenses', ExpenseView.as_view()),
    path('expenses/<str:pk>', ExpenseDetailView.as_view()),
    path('expenses/<str:pk>/comments', CommentListView.as_view()),
    path('totals', TotalView.as_view()),
    path('activites', ActivityListView.as_view()),
    path('activites/<int:pk>', ActivityRetrieveView.as_view())
]
