from django.conf.urls import url
from .views import PostListView,PostDetailView,PostCreateView, PostUpdateView, PostDeleteView
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url('', PostListView.as_view(), name = 'insta-home' ),
    url('post/<int:pk>/', PostDetailView.as_view(), name = 'post-detail' ),
    url('post/new/', PostCreateView.as_view(), name = 'post-create' ),
    url('post/<int:pk>/update/', PostUpdateView.as_view(), name = 'post-update' ),
    url('post/<int:pk>/delete/', PostDeleteView.as_view(), name = 'post-delete' ),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
