from django.urls import path
from .views import ArticleListView, ArticleUpdateView, ArticleDeleteView, ArticleDetailView, ArticleCreateView

urlpatterns = [
    path('', ArticleListView.as_view(), name='article_list'),
    path('<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
    path('<int:pk>/update', ArticleUpdateView.as_view(), name='article_update'),
    path('<int:pk>/delete/', ArticleDeleteView.as_view(), name='article_delete'),
    path('create/', ArticleCreateView.as_view(), name='article_create'),

]
