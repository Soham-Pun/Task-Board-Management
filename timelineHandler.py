import jinja2
import webapp2
import os
from google.appengine.ext import ndb
from google.appengine.api import users
from myuser import MyUser
from FollowAndFollowers import Follow_And_Followers
from google.appengine.ext import blobstore
from uploadHandler import UploadHandler
from captionHandler import CaptionHandler
from downloadHandler import DownloadHandler
from searchHandler import SearchHandler
from othersProfilePage import OthersProfilePageHandler
from followHandler import FollowHandler
from profile_page import ProfilePageHandler
from followerListHandler import FollowerListHandler
from followListHandler import FollowingListHandler
from addCommentsHandler import AddCommentHandler
from viewCommentHandler import ViewCommentHandler

jinja2_env = jinja2.Environment(loader=jinja2.FileSystemLoader(os.getcwd()), extensions=['jinja2.ext.autoescape'],
                                autoescape=True)

class TimelineHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()

        if user == None:
            login_url = users.create_login_url(self.request.path)
            template_value = {"login_url": login_url}
            template = jinja2_env.get_template("guest.html")
            self.response.write(template.render(template_value))
            return

        else:
            myuser_key = ndb.Key('MyUser', user.user_id())
            myuser = myuser_key.get()
            logout_url = users.create_logout_url(self.request.path)

            if myuser == None:
                template = jinja2_env.get_template("AddName.html")
                self.response.write(template.render())
                return

            timeLinePics = []


            if len(myuser.timeLinePics)>=50:
                for i in range(0,50):
                    timeLinePics.append(myuser.timeLinePics[i].get())

            else:
                for i in myuser.timeLinePics:
                    timeLinePics.append(i.get())

            picsUploadedBy = []
            for j in timeLinePics:
                picsUploadedBy.append(j.uploadedBy.get())



            template_values = {"timeLinePics":timeLinePics,
                               "logout_url":logout_url,
                               "picsUploadedBy":picsUploadedBy,
                               "myuser":myuser}
            template = jinja2_env.get_template("timeline.html")
            self.response.write(template.render(template_values))





class AddNameHandler(webapp2.RequestHandler):
    def post(self):
        user = users.get_current_user()
        user_name = self.request.get("name")
        myuser = MyUser(id=user.user_id())
        myuser.name = user_name
        follow_and_followers_obj = Follow_And_Followers()
        follow_and_followers_obj.put()
        myuser.followAndFollower = follow_and_followers_obj.key
        myuser.put()

        self.response.write("""<script> window.location = '/'; </script>""")



app = webapp2.WSGIApplication([('/', TimelineHandler),('/AddNameHandler', AddNameHandler),
                               ('/upload', UploadHandler),
                               ('/captionHandler', CaptionHandler),
                               ('/downloadHandler', DownloadHandler),
                               ('/searchHandler', SearchHandler),
                               ('/othersProfilePage', OthersProfilePageHandler),
                               ('/followHandler', FollowHandler),
                               ('/profilePageHandler', ProfilePageHandler),
                               ('/followerListHandler', FollowerListHandler),
                               ('/followListHandler', FollowingListHandler),
                               ('/addCommentsHandler', AddCommentHandler),
                               ('/viewCommentHandler', ViewCommentHandler)],debug=True)





