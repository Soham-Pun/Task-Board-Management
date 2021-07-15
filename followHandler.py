import jinja2
import webapp2
import os
from google.appengine.ext import ndb
from google.appengine.api import users
from myuser import MyUser
from FollowAndFollowers import Follow_And_Followers


jinja2_env = jinja2.Environment(loader=jinja2.FileSystemLoader(os.getcwd()), extensions=['jinja2.ext.autoescape'],
                                autoescape=True)

class FollowHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        myuser_key = ndb.Key('MyUser', user.user_id())
        myuser = myuser_key.get()

        otherUser_key = ndb.Key('MyUser', self.request.get("key_id"))
        otherUser = otherUser_key.get()

        status = self.request.get("status")

        if status == "True":
            myuser_follow_obj = myuser.followAndFollower.get()
            myuser_follow_obj.follows.remove(otherUser_key)
            for i in otherUser.my_post:
                myuser.timeLinePics.remove(i)
            myuser.put()

            myuser_follow_obj.put()

            otherUser_follow_obj = otherUser.followAndFollower.get()
            otherUser_follow_obj.followers.remove(myuser_key)
            otherUser_follow_obj.put()

        else:
            myuser_follow_obj = myuser.followAndFollower.get()
            myuser_follow_obj.follows.append(otherUser_key)
            for i in range(len(otherUser.my_post)-1, -1 , -1):
                myuser.timeLinePics.insert(0,otherUser.my_post[i])
            myuser.put()
            myuser_follow_obj.put()

            otherUser_follow_obj = otherUser.followAndFollower.get()
            otherUser_follow_obj.followers.append(myuser_key)
            otherUser_follow_obj.put()

        key_id = self.request.get("key_id")
        template_values = {"key_id":key_id}
        template = jinja2_env.get_template("redirectingToOPP.html")
        self.response.write(template.render(template_values))
