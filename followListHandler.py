import jinja2
import webapp2
import os
from google.appengine.ext import ndb
from myuser import MyUser

jinja2_env = jinja2.Environment(loader=jinja2.FileSystemLoader(os.getcwd()), extensions=['jinja2.ext.autoescape'],
                                autoescape=True)


class FollowingListHandler(webapp2.RequestHandler):
    def get(self):
        userKey = ndb.Key('MyUser', self.request.get("key_id"))
        user = userKey.get()

        followAndFollower_obj = user.followAndFollower.get()

        followingList = []
        for i in followAndFollower_obj.follows:
            followingList.append(i.get())

        template_value = {"followingList": followingList}
        template = jinja2_env.get_template("followingList.html")
        self.response.write(template.render(template_value))