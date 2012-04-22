import urllib2
import json

def get_artist_cloudcasts(artistname,offset=0):
  offset=12*int(offset)
  url='http://api.mixcloud.com/artist/'+artistname+'/popular/?limit=12&offset='+str(offset)
  try:
    page=urllib2.urlopen(url)
    cloudcasts=json.loads(''.join(page.readlines()))
    if 'error' in cloudcasts:
      return {}
    else:
      return cloudcasts
  except:
    return {}