from django.conf.urls import patterns, url
from voxpop import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	#url(r'^suggest_firm/$', views.suggest_firm, name='suggest_firm'),
	url(r'^firms/$', views.firms, name='firms'),
	url(r'^show_reviews/$', views.show_reviews, name='show_reviews'),
	url(r'^newhome/$', views.newhome, name='newhome'),
	url(r'^newreview/$', views.newreview, name='newreview'),
	)