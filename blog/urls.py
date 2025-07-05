from django.urls import path
from . import views

# If you make a typying mistake(typo) "urlpatterns", You can't run server.
urlpatterns = [
    #path arg1:designate letters pattern on URL 2:the view to be called when URL pattern is matched 3:pattern's name
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
]