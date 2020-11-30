from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList, name='home'),
    path(r'create', views.openEditor, name='create_new'),
    path(r'save', views.addList, name="save_new"),
    path(r'post/<int:blog_id>', views.PostDetail, name='post_detail'),
    path(r'like/<int:blog_id>', views.update_like),
]