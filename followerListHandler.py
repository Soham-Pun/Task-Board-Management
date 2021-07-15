import jinja2
import webapp2
import os
from google.appengine.ext import ndb
from myuser import MyUser


jinja2_env = jinja2.Environment(loader=jinja2.FileSystemLoader(os.getcwd()), extensions=['jinja2.ext.autoescape'],
                                autoescape=True)

class FollowerListHandler(webapp2.RequestHandler):
    def get(self):
        userKey = ndb.Key('MyUser', self.request.get("key_id"))
        user = userKey.get()

        followAndFollower_obj = user.followAndFollower.get()

        followerList = []
        for i in followAndFollower_obj.followers:
            followerList.append(i.get())

        template_value = {"followerList":followerList}
        template = jinja2_env.get_template("followerList.html")
        self.response.write(template.render(template_value))