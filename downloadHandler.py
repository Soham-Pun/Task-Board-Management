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

class DownloadHandler(blobstore_handlers.BlobstoreDownloadHandler):
    def get(self):
        self.send_blob(self.request.get("blobkeyid"))
