import jinja2
import webapp2
import os
from google.appengine.ext import ndb
from google.appengine.api import users
from myuser import MyUser
from google.appengine.ext import blobstore
from google.appengine.ext.webapp import blobstore_handlers

jinja2_env = jinja2.Environment(loader=jinja2.FileSystemLoader(os.getcwd()), extensions=['jinja2.ext.autoescape'],
                                autoescape=True)

class CaptionHandler(webapp2.RequestHandler):
    def get(self):
        picPostKeyId = long(self.request.get("picPostKeyId"))

        template_value = {"picPostKeyId":picPostKeyId}
        template = jinja2_env.get_template("caption.html")
        self.response.write(template.render(template_value))



    def post(self):
        caption = self.request.get("caption")
        picPostKeyId = long(self.request.get("picPostKeyId"))

        picPostKey = ndb.Key('Post', picPostKeyId)
        picPost = picPostKey.get()

        picPost.caption = caption
        picPost.put()

        self.redirect('/profilePageHandler')



