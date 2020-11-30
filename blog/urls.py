from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),

    # 詳細画面
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    # 投稿画面
    path('post/new/', views.post_new, name='post_new'),
    # 編集画面
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    # 草稿画面
    path('drafts/', views.post_draft_list, name='post_draft_list'),
    # 公開
    path('post/<pk>/publish/', views.post_publish, name='post_publish'),
    # 削除
    path('post/<pk>/remove/', views.post_remove, name='post_remove'),
    # コメント
    path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),

    path('comment/<int:pk>/approve/', views.comment_approve, name='comment_approve'),
    path('comment/<int:pk>/remove/', views.comment_remove, name='comment_remove'),
]