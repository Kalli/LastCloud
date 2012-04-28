# Create your views here.
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from managers import lastfm_manager, mixcloud_manager
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from forms import LastFmUserNameForm, LastFmArtistForm
import re


def index(request):
  params={}
  if request.method=='POST':
    if 'username' in request.POST:
      userform = LastFmUserNameForm(request.POST)
      if userform.is_valid():
        lastfm_username=userform.cleaned_data['username']
        period=userform.cleaned_data['period']
        params={'redirecturl':'/lastcloud/lastfm/user/'+lastfm_username+'/?period='+period}
      else:
        params={'userform':userform,'artistform':LastFmArtistForm()}
    if 'artistname' in request.POST:
      artistform=LastFmArtistForm(request.POST)
      if artistform.is_valid():
        artistname=artistform.cleaned_data['artistname']
        params={'redirecturl':'/lastcloud/lastfm/artist/'+artistname+'/similar'}
      else:
        params={'userform':LastFmUserNameForm(),'artistform':artistform}
  else:
    params={'userform':LastFmUserNameForm(),'artistform':LastFmArtistForm()}
  if 'redirecturl' in params:
    return HttpResponseRedirect(params['redirecturl'])
  else: 
    return render_to_response('index.html',params,context_instance=RequestContext(request))
  
def get_lastfm_users_topartists(request,lastfm_username,page=1,period='overall'):
  if 'period' in request.GET:
    period=request.GET['period']
  top_artists=lastfm_manager.get_user_top_artists(lastfm_username,page,period)
  if(type(top_artists)==str):
    params={'lastfm_username':lastfm_username, 'page':page}
  else:
    params={'artists':top_artists,'lastfm_username':lastfm_username, 'page':page}
  return render_to_response('users_top_artists.html',params,context_instance=RequestContext(request))

def get_lastfm_similar_artists(request, artistname, page=1):
  similar_artists=lastfm_manager.get_similar_artists(artistname,page)
  if(type(similar_artists)==str):
    params={'page':page, 'artistname':artistname.replace("+"," ").title()}
  else:
    params={'artists':similar_artists,'artistname':artistname.replace("+"," ").title(),'page':page}
  return render_to_response('similar_artists.html',params,context_instance=RequestContext(request))


def get_lastfm_top_artists(request,page=0):
  top_artists=lastfm_manager.get_top_artists(page)
  if(type(top_artists)==str):
    params={'page':page, 'artistname':"Top Last.fm Artists"}
  else:
    params={'artists':top_artists,'artistname':"Top Last.fm Artists",'page':page}
  return render_to_response('top_artists.html',params,context_instance=RequestContext(request))
    
    
def get_mixcloud_mixes(request,mixcloud_artist,offset=0):
  artist_mixes=mixcloud_manager.get_artist_cloudcasts(mixcloud_artist,offset)
  artistname=mixcloud_artist.replace("-"," ").title()
  if artist_mixes:
    if 'lastfmusername' in request.GET:
      lastFmUsername=request.GET['lastfmusername']
      params={'mixes':artist_mixes,'artist':mixcloud_artist,'offset':offset, 'lastFmUsername':lastFmUsername,'artistname':artistname}
    else:
      params={'mixes':artist_mixes,'artist':mixcloud_artist,'offset':offset,'artistname':artistname}
  else:
    params={'artist':mixcloud_artist,'offset':"1",'artistname':artistname}
  return render_to_response('mixcloud_artist_mixes.html',params,context_instance=RequestContext(request))