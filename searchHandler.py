import jinja2
import webapp2
import os

from myuser import MyUser


jinja2_env = jinja2.Environment(loader=jinja2.FileSystemLoader(os.getcwd()), extensions=['jinja2.ext.autoescape'],
                                autoescape=True)

class SearchHandler(webapp2.RequestHandler):
    def get(self):
        search = self.request.get("search")

        allUser = MyUser.query().fetch()


        userResult = []
        for i in allUser:
            if i.name.lower().startswith(search.lower()):
                userResult.append(i)


        template_value = {"userResult":userResult}
        template = jinja2_env.get_template("searchResult.html")
        self.response.write(template.render(template_value))


