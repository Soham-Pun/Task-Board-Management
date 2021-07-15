from google.appengine.ext import ndb
from post import Post
from FollowAndFollowers import Follow_And_Followers

class MyUser(ndb.Model):
    name = ndb.StringProperty()
    followAndFollower = ndb.KeyProperty(kind=Follow_And_Followers)
    my_post = ndb.KeyProperty(kind=Post, repeated=True)
    timeLinePics = ndb.KeyProperty(kind=Post, repeated=True)