from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static





urlpatterns=[
    url(r'^$',views.daily_post,name='postToday'),
    # url(r'^archives/(\d{4}-\d{2}-\d{2})/$',views.past_days_news,name = 'pastNews')·,
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^post/(\d+)',views.post,name ='post'),
    # URLConf for new article view
    url(r'^new/post$', views.new_post, name='new-post'),
    url(r'^profile/',views.profile,name = 'Profile'),
    url(r'^edit/profile/$',views.edit_profile,name = 'edit-profile'),
    url(r'^project-vote/(\d+)',views.vote_project,name = 'project-vote'),




]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)