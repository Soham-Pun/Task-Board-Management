from google.appengine.ext import ndb

class Follow_And_Followers(ndb.Model):
    follows = ndb.KeyProperty(repeated=True)
    followers = ndb.KeyProperty(repeated=True)

