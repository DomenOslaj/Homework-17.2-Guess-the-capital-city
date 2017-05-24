#!/usr/bin/env python
import os
import jinja2
import webapp2


template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=False)


class BaseHandler(webapp2.RequestHandler):

    def write(self, *a, **kw):
        return self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        return self.write(self.render_str(template, **kw))

    def render_template(self, view_filename, params=None):
        if not params:
            params = {}
        template = jinja_env.get_template(view_filename)
        return self.response.out.write(template.render(params))


class MainHandler(BaseHandler):
    def get(self):
        return self.render_template("main.html")

class Data(object):
    def __init__(self, country, capital, image):
        self.country = country
        self.capital = capital
        self.image = image

lj = Data(country="Slovenia", capital="Ljubljana", image="/assets/img/capital_1.png")
vi = Data(country="Austria", capital="Vienna", image="/assets/img/capital_2.png")
be = Data(country="Germany", capital="Berlin", image="/assets/img/capital_3.png")
bu = Data(country="Hungary", capital="Budapest", image="/assets/img/capital_4.jpg")
he = Data(country="Finland", capital="Helsinki", image="/assets/img/capital_5.png")
br = Data(country="Belgium", capital="Brussels", image="/assets/img/capital_6.png")



app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
], debug=True)
