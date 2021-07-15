from google.appengine.ext import ndb
from comments import Comments

class Post(ndb.Model):
    filename = ndb.StringProperty()
    comments = ndb.StructuredProperty(Comments,repeated=True)
    caption = ndb.StringProperty()
    pic = ndb.BlobKeyProperty()
    uploadedBy = ndb.KeyProperty()
