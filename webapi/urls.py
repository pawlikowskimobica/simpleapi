from django.conf.urls import patterns, include, url
import views
urlpatterns = patterns('',
    url(r'^client/$', views.ClientView.as_view()),
    url(r'^pair/$', views.PairView.as_view()),
)
