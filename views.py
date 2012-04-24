# Create your views here.
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from managers import lastfm_manager, mixcloud_manager
from django.core.urlresolvers import reverse
from django import forms
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import re

def index(request):
  if request.method=='POST':
    form = LastFmUserNameForm(request.POST)
    if form.is_valid():
      lastfm_username=form.cleaned_data['username']
      period=form.cleaned_data['period']
      return HttpResponseRedirect('/lastcloud/lastfmusername/'+lastfm_username+'/?period='+period)
    else:
      return render_to_response('index.html',{'form':form},context_instance=RequestContext(request)) 
  else:
    form=LastFmUserNameForm()
  return render_to_response('index.html',{'form':form},context_instance=RequestContext(request))
  
def get_lastfm_users_topartists(request,lastfm_username,page=1,period='overall'):
  if 'period' in request.GET:
    period=request.GET['period']
  top_artists=lastfm_manager.get_top_artists(lastfm_username,page,period)
  if(type(top_artists)==str):
    return render_to_response('users_top_artists.html',{'lastfm_username':lastfm_username, 'page':page},context_instance=RequestContext(request))
  else:
    return render_to_response('users_top_artists.html',{'artists':top_artists,'lastfm_username':lastfm_username, 'page':page},context_instance=RequestContext(request))

def get_lastfm_similar_artists(request, artistname, page=1):
  similar_artists=lastfm_manager.get_similar_artists(artistname,page)
  if(type(similar_artists)==str):
    return render_to_response('similar_artists.html',{'page':page, 'artistname':artistname.replace("+"," ").title()},context_instance=RequestContext(request))
  else:
    return render_to_response('similar_artists.html',{'artists':similar_artists,'artistname':artistname.replace("+"," ").title(),'page':page},context_instance=RequestContext(request))
  
    
def get_mixcloud_mixes(request,mixcloud_artist,offset=0):
  artist_mixes=mixcloud_manager.get_artist_cloudcasts(mixcloud_artist,offset)
  artistname=mixcloud_artist.replace("-"," ").title()
  if artist_mixes:
    if 'lastfmusername' in request.GET:
      lastFmUsername=request.GET['lastfmusername']
      return render_to_response('mixcloud_artist_mixes.html',{'mixes':artist_mixes,'artist':mixcloud_artist,'offset':offset, 'lastFmUsername':lastFmUsername,'artistname':artistname},context_instance=RequestContext(request))
    else:
      return render_to_response('mixcloud_artist_mixes.html',{'mixes':artist_mixes,'artist':mixcloud_artist,'offset':offset,'artistname':artistname},context_instance=RequestContext(request))
  else:
    return render_to_response('mixcloud_artist_mixes.html',{'artist':mixcloud_artist,'offset':"1",'artistname':artistname},context_instance=RequestContext(request))

PERIODS=(
        ('overall', 'All time'),
        ('12month', 'Last year'),
        ('6month', 'Last six months'),
        ('3month', 'Last three months'),
        ('7day', 'Last week'),
)

class LastFmUserNameForm(forms.Form):
  username=forms.CharField(max_length=100)
  period=forms.ChoiceField(choices=PERIODS)
  def clean(self):
    cleaned_data = super(LastFmUserNameForm, self).clean()
    username = self.cleaned_data['username']
    period = self.cleaned_data['period']
    if not re.search(r'^\w+', username):
      msg = u"Username can only contain alphanumeric characters and the underscore."
      self._errors["username"] = self.error_class([msg])
    if period not in ['overall','12month','6month','3month','7day']:
      msg=u"You must select one of the periods"
      self._errors["period"] = self.error_class([msg])
    return cleaned_data
    