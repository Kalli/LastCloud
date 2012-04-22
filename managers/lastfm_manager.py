import urllib2 
import json
from django.conf import settings

#Your last.fm api key should be defined in your settings.py or similar
def get_top_artists(username, page=0):  
  url="http://ws.audioscrobbler.com/2.0/?method=user.gettopartists&user="+username+"&api_key="+settings.API_KEY+"&format=json&page="+str(page)
  try:
    page=urllib2.urlopen(url)
    content=''.join(page.readlines()).replace("#text","text")
    artists=json.loads(content)
    if 'error' in artists:
      return "user not found"
    else:
      return artists
  except:
    return "user not found"

def get_similar_artists(artistname,page):
  artistname=artistname.replace("-","+")
  url="http://ws.audioscrobbler.com/2.0/?method=artist.getsimilar&artist="+artistname+"&api_key="+settings.API_KEY+"&format=json&page="+str(page)
  try:
    page=urllib2.urlopen(url)
    content=''.join(page.readlines()).replace("#text","text")
    artists=json.loads(content)
    if 'error' in artists:
      return "artist not found"
    else:
      return artists
  except:
    return "artist not found"