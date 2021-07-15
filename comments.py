from google.appengine.ext import ndb

class Comments(ndb.Model):
    user = ndb.StringProperty()
    text = ndb.TextProperty()
