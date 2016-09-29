from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    url(r'^$',views.home,name='home'),
    url(r'^list/$', views.post_list, name='post_list'),
    url(r'^posts/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    url(r'^posts/new/$', views.post_new, name='post_new'),
    url(r'^posts/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^posts/(?P<pk>\d+)/delete/$',views.post_remove, name='post_remove'),
    url(r'^deletepost/$', views.post_draft_list, name='post_draft_list'),
    url(r'^post/(?P<pk>\d+)/publish/$', views.post_publish, name='post_publish'),
    url(r'^posts/(?P<pk>\d+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
    url(r'^comment/(?P<pk>\d+)/approve/$', views.comment_approve, name='comment_approve'),
    url(r'^comment/(?P<pk>\d+)/remove/$', views.comment_remove, name='comment_remove'),
    url(r'^popup/$',views.popup),
    url(r'^posts/(?P<pk>\d+)/realdelete/$',views.post_realremove, name='post_realremove'),
    url(r'^signup/$', views.signup, name='signup'),





]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
