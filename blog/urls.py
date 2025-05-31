from django.urls import path
from . import views

# If you make a typying mistake(typo) "urlpatterns", You can't run server.
urlpatterns = [
    #path arg1:designate letters pattern on URL 2:the view to be called when URL pattern is matched 3:pattern's name
    path('', views.post_list, name='post_list'),
]