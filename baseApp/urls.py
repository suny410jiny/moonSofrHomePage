from django.urls import path
from baseApp import views

app_name = 'baseApp'

urlpatterns = [
    path('', views.index, name='index'),
    path('post/new/',views.post_new,name='post_new'),
    path('post/prod/', views.post_list_prod, name='post_list_prod'),
    path('post/project/', views.post_list_project, name='post_list_project'),
    path('post/prod/<int:pk>/',views.post_detail_prod,name='post_detail_prod'),
    path('post/project/<int:pk>/',views.post_detail_project,name='post_detail_project'),
    # path('post/<int:pk>/like',views.post_like,name='post_like'),
    # path('post/<int:pk>/unlike',views.post_unlike,name='post_unlike'),
    # path('post/<int:post_pk>/comment/new',views.comment_new,name='comment_new'),
    # re_path(r'^(?P<username>[\w.@+-]+)/$', views.user_page,name='user_page'),
]