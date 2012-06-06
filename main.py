import webapp2
from google.appengine.ext.webapp import template
from google.appengine.api import users
from login import LoginHandler

class HomeHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if users.is_current_user_admin():
            loggedin = "Admin"
            values = {'loggedin': loggedin,
                      'login_url': users.create_login_url("/"),
                      'logout_url': users.create_logout_url("/")}
        elif user:
            loggedin = "User"
            values = {'loggedin': loggedin,
                      'login_url': users.create_login_url("/"),
                      'logout_url': users.create_logout_url("/")}
        else:
            loggedin = "Anonymous"
            values = {'loggedin': loggedin,
                      'login_url': users.create_login_url("/"),
                      'logout_url': users.create_logout_url("/")}
        self.response.out.write(template.render('home.html', values))

app = webapp2.WSGIApplication([
    webapp2.Route(r'/', HomeHandler),
    webapp2.Route(r'/login', LoginHandler, schemes=['https'])
], debug=True)
