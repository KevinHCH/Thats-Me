import os
from flask import Flask, Blueprint

# The correct way to import custom modules in Flask App
from .config import config

PORT = config.PORT
DEBUG = config.DEBUG

app = Flask(__name__,static_url_path="/storage", static_folder="storage", template_folder="templates")
#register another STATIC FOLDER
blueprint = Blueprint('site', __name__, static_url_path='/static', static_folder='static') 
app.register_blueprint(blueprint)
app.secret_key = config.SECRET
from . import views

methods = ["GET", "POST"]

# MIDDLEWARES
# All the request will pass this function 
# app.before_request(views.router_middleware)

# ROUTES
app.add_url_rule('/', view_func=views.index)
app.add_url_rule('/images', view_func=views.list_all_images)
app.add_url_rule('/about', view_func=views.about)
app.add_url_rule('/login', methods=methods, view_func=views.admin_login)
app.add_url_rule('/admin', methods=methods, view_func=views.admin)
app.add_url_rule("/admin/", view_func=views.index_admin)
app.add_url_rule('/admin/images', methods=methods, view_func=views.add_img)
app.add_url_rule("/admin/about", methods=methods, view_func=views.edit_about)

# This enable the autoreload server
if __name__ == "__main__":
    app.run('0.0.0.0', PORT,debug=DEBUG, use_reloader=True)