import jinja2
import webapp2
import os
from google.appengine.ext import ndb
from google.appengine.api import users
from myuser import MyUser
from FollowAndFollowers import Follow_And_Followers
from google.appengine.ext import blobstore
from comments import Comments


jinja2_env = jinja2.Environment(loader=jinja2.FileSystemLoader(os.getcwd()), extensions=['jinja2.ext.autoescape'],
                                autoescape=True)

class AddCommentHandler(webapp2.RequestHandler):
    def get(self):
        postKeyId = long(self.request.get("postKeyId"))
        name = self.request.get("name")

        template_value = {"postKeyId":postKeyId,
                          "name":name}
        template = jinja2_env.get_template("addComment.html")
        self.response.write(template.render(template_value))

    def post(self):
        postKeyId = long(self.request.get("postKeyId"))
        name = self.request.get("name")

        post_key = ndb.Key('Post', postKeyId)
        post_obj = post_key.get()
        comment_obj = Comments()
        comment_obj.text = self.request.get("comment")
        comment_obj.user = name
        comment_obj.put()

        post_obj.comments.insert(0, comment_obj)
        post_obj.put()

        self.redirect('/')
