from django.utils import unittest
from managers import lastfm_manager, mixcloud_manager
from lastcloud import views
from django.test import Client

class ManagerTestCase(unittest.TestCase):
  def setUp(self):
    self.lastfm_manager=lastfm_manager
    self.mixcloud_manager=mixcloud_manager
    
  def test_get_top_artists(self):
    response=lastfm_manager.get_user_top_artists("djkalli", "1", "overall")
    self.assertTrue(type(response)==dict, "The response should be a dict")
    self.assertEquals(response['topartists']['@attr']['user'],"djkalli")
    
  def test_get_similar_artists(self):
    response=lastfm_manager.get_similar_artists("Portishead","1")
    self.assertTrue(type(response)==dict, "The response should be a dict")
    self.assertEquals(response['similarartists']['@attr']['artist'],"Portishead")
    
class WebTestCase(unittest.TestCase):
  def test_views(self):
    client=Client()
    urls=[
      "/lastcloud/",
      "/lastcloud/lastfm/user/djkalli/",
      "/lastcloud/lastfm/user/djkalli",
      "/lastcloud/lastfm/artist/zomby/similar/",
      "/lastcloud/lastfm/artist/Andy%20Stott/similar/",
      "/lastcloud/lastfm/topartists/"
    ]
    for url in urls:
      response = client.get(url)
      self.assertEquals(response.status_code,200)
    
