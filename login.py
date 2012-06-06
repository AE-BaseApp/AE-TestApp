import webapp2
from google.appengine.ext.webapp import template
from google.appengine.api import users

#  Login page Request Handler Class
class LoginHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()

        values = {'login_url': users.create_login_url("/")}
        self.response.out.write(template.render('login.html', values))
