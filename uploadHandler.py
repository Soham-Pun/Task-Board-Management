import jinja2
import webapp2
import os
from google.appengine.ext import ndb
from google.appengine.api import users
from myuser import MyUser
from post import Post
from google.appengine.ext import blobstore
from google.appengine.ext.webapp import blobstore_handlers

jinja2_env = jinja2.Environment(loader=jinja2.FileSystemLoader(os.getcwd()), extensions=['jinja2.ext.autoescape'],
                                autoescape=True)

class UploadHandler(blobstore_handlers.BlobstoreUploadHandler):

    def post(self):
        user = users.get_current_user()
        myuser_key = ndb.Key('MyUser', user.user_id())
        myuser = myuser_key.get()

        upload = self.get_uploads()[0]
        blobinfo = blobstore.BlobInfo(upload.key())
        picPost = Post()

        picPost.filename = blobinfo.filename
        picPost.pic = upload.key()
        picPost.uploadedBy = myuser_key
        picPost.put()



        picPost_key = picPost.key
        myuser.my_post.insert(0,picPost_key)
        myuser.timeLinePics.insert(0, picPost_key)
        myuser.put()

        followAndFollower_obj = myuser.followAndFollower.get()
        allfollowers = []

        for j in followAndFollower_obj.followers:
            allfollowers.append(j.get())

        for i in allfollowers:
            i.timeLinePics.insert(0, picPost_key)
            i.put()




        template_value = {"picPostKeyId":picPost_key.id()}
        template = jinja2_env.get_template("caption.html")
        self.response.write(template.render(template_value))


