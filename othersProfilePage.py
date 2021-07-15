import jinja2
import webapp2
import os
from google.appengine.ext import ndb
from google.appengine.api import users
from myuser import MyUser


jinja2_env = jinja2.Environment(loader=jinja2.FileSystemLoader(os.getcwd()), extensions=['jinja2.ext.autoescape'],
                                autoescape=True)

class OthersProfilePageHandler(webapp2.RequestHandler):
    def get(self):

        user = users.get_current_user()
        myuser_key = ndb.Key('MyUser', user.user_id())
        myuser = myuser_key.get()
        logout_url = users.create_logout_url('/')

        # otheruserKeyId = long(self.request.get("key_id"))
        otheruserKey = ndb.Key('MyUser', self.request.get("key_id"))
        otheruser = otheruserKey.get()

        if otheruser == myuser:
            self.redirect('/')
            return

        follow_status = False
        if myuser.followAndFollower != None:
            followAndFollower_obj = myuser.followAndFollower.get()

            for i in followAndFollower_obj.follows:
                if i == otheruserKey:
                    follow_status = True
                    break

        follow_size = 0
        follower_size = 0
        if otheruser.followAndFollower != None:
            followAndFollower_obj = otheruser.followAndFollower.get()

            follow_size = len(followAndFollower_obj.follows)
            follower_size = len(followAndFollower_obj.followers)


        otheruser_post = []
        for i in otheruser.my_post:
            otheruser_post.append(i.get())


        template_values = {"otheruser_post":otheruser_post,
                           "follow_status":follow_status,
                           "follow_size":follow_size,
                           "follower_size":follower_size,
                           "logout_url":logout_url,
                           "otheruser":otheruser,
                           "myuser":myuser}

        template = jinja2_env.get_template("othersProfilePage.html")
        self.response.write(template.render(template_values))



