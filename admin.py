import webapp2
from google.appengine.ext.webapp import template
from google.appengine.api import users

#  Login page Request Handler Class
class AdminHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()

        values = {'user': user.nickname()}
        self.response.out.write(template.render('admin.html', values))
