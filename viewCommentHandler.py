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

class ViewCommentHandler(webapp2.RequestHandler):
    def get(self):
        postKeyId = long(self.request.get("postKeyId"))

        post_key = ndb.Key('Post', postKeyId)
        post_obj = post_key.get()

        allComments = []

        for i in post_obj.comments:
            allComments.append(i)

        template_values = {"allComments":allComments}
        template = jinja2_env.get_template("viewComments.html")
        self.response.write(template.render(template_values))