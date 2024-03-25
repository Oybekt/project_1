from django.urls import path
from blog import views

app_name = "blog"

urlpatterns = [
    path('', views.home, name="home"),
    path('search/<str:query>/', views.search, name="search"),
    path('category/<str:query>/', views.category, name="category"),
    path('post_detail/<int:id>/', views.post_detail, name='post_detail' ),
    path('post_create/', views.post_create, name='post_create'),
    path('post_update/<int:id>/', views.post_update, name='post_update'),
    path('post_delete/<int:id>/', views.post_delete, name='post_delete'),
    path('<int:post_id>/like/', views.like_post, name='like_post'),
]
