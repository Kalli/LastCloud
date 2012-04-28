from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('lastcloud.views',
  url(r'^$', 'index'),
  # handle urls with empty parameters
  url('lastfm[/]?$', 'index'),
  url('lastfm/user[/]?$', 'index'),
  url('mixcloud/artist[/]?$', 'index'),
  url('mixcloud[/]?$', 'index'),
  url('lastfm/artist/$', 'index'),
  
  # get mixcloud mixes
  url('mixcloud/artist/(?P<mixcloud_artist>[\w | -]+)/$','get_mixcloud_mixes'),
  url('mixcloud/artist/(?P<mixcloud_artist>[\w | -]+)/(?P<offset>\d)','get_mixcloud_mixes'),
    
  # get last.fm data
  url('lastfm/user/(?P<lastfm_username>[\w | -]+)[/]?$', 'get_lastfm_users_topartists'),
  url('lastfm/user/(?P<lastfm_username>[\w | -]+)/(?P<page>\d)', 'get_lastfm_users_topartists'),
  url('lastfm/artist/(?P<artistname>[\w | - | + | (%20) | &]+)[/]$', 'get_lastfm_similar_artists'),
  url('lastfm/artist/(?P<artistname>[\w | - | + | (%20) | &]+)[/]similar', 'get_lastfm_similar_artists'),
  url('lastfm/topartists/','get_lastfm_top_artists')
  )