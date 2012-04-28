from django import forms
import re


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
    if re.search(r'[\s]',username):
      msg = u"Username can only contain alphanumeric characters and the underscore."
      self._errors["username"] = self.error_class([msg])
    if period not in ['overall','12month','6month','3month','7day']:
      msg=u"You must select one of the periods"
      self._errors["period"] = self.error_class([msg])
    return cleaned_data

class LastFmArtistForm(forms.Form):
  artistname=forms.CharField(max_length=100)
  def clean(self):
    cleaned_data = super(LastFmArtistForm, self).clean()
    artistname = self.cleaned_data['artistname']
    return cleaned_data

