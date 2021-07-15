import jinja2
import webapp2
import os
from google.appengine.ext import ndb
from google.appengine.api import users
from myuser import MyUser
from FollowAndFollowers import Follow_And_Followers
from google.appengine.ext import blobstore


jinja2_env = jinja2.Environment(loader=jinja2.FileSystemLoader(os.getcwd()), extensions=['jinja2.ext.autoescape'],
                                autoescape=True)

class ProfilePageHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()


        myuser_key = ndb.Key('MyUser', user.user_id())
        myuser = myuser_key.get()
        logout_url = users.create_logout_url('/')

        alluser = MyUser.query().fetch()
        upload_url = blobstore.create_upload_url('/upload')

        my_post_key = myuser.my_post
        my_post_obj = []
        for i in my_post_key:
            my_post_obj.append(i.get())

        follow_size = len(myuser.followAndFollower.get().follows)
        follower_size = len(myuser.followAndFollower.get().followers)




        template_values = {"myuser":myuser,
                            "upload_url":upload_url,
                            "alluser":alluser,
                            "my_post_obj":my_post_obj,
                            "logout_url":logout_url,
                            "follow_size":follow_size,
                            "follower_size":follower_size}


        template = jinja2_env.get_template("ProfilePage.html")
        self.response.write(template.render(template_values))




