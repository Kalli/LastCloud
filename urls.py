from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('lastcloud.views',
  url(r'^$', 'index'),
  # handle urls with empty parameters
  url('lastfmusername/$', 'index'),
  url('mixcloudartist/$', 'index'),
  url('similarartists/$', 'index'),
  
  # get mixcloud mixes
  url('mixcloudartist/(?P<mixcloud_artist>[\w | -]+)/$','get_mixcloud_mixes'),
  url('mixcloudartist/(?P<mixcloud_artist>[\w | -]+)/(?P<offset>\d)','get_mixcloud_mixes'),
    
  # get last.fm data
  url('lastfmusername/(?P<lastfm_username>\w+)/$', 'get_lastfm_users_topartists'),
  url('lastfmusername/(?P<lastfm_username>\w+)/(?P<page>\d)', 'get_lastfm_users_topartists'),
  url('similarartists/(?P<artistname>[\w | - | + | (%20) | &]+)[/]$', 'get_lastfm_similar_artists'),
  url('similarartists/(?P<artistname>[\w | - | + | (%20) | &]+)[/](?P<page>\d)', 'get_lastfm_similar_artists')
  )