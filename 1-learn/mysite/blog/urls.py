from django.conf.urls import patterns, include, url
from django.views.generic import ListView, DetailView
from blog.models import Post
from blog import views
urlpatterns=patterns('',
		 url(r'^$', ListView.as_view (
                         queryset=Post.objects.all().order_by("-date")[:10], #-date for reverse chrono order
                         template_name="blog.html")),
                 url(r'^(?P<pk>\d+)$', DetailView.as_view (
                         	     model = Post,
				     template_name="post.html")),
                 url(r'^archives/$', ListView.as_view (
                         queryset=Post.objects.all().order_by("-date"), #-date for reverse chrono order
                         template_name="archives.html")),
                 url(r'^latestnews/$', ListView.as_view (
                         queryset=Post.objects.all().order_by("-date")[:5], #-date for reverse chrono order
                         template_name="latestnews.html")),
		url(r'^sample_graph/$', views.graph, name="graph"),
)
