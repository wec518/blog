from flask import Blueprint
from blog import db
from blog import myAdmin 
from flask_admin import Admin, BaseView, expose
from blog.models import User, Post
from flask_admin.contrib.sqla import ModelView
from flask_login import login_user, current_user

blogAdmin = Blueprint('blogAdmin', __name__)

class MyView(BaseView):
  
    def is_accessible(self):
        return current_user.email == "weichi_chen@hotmail.com"

class MicroBlogModelView(ModelView):
    can_delete = True  # disable model deletion
    page_size = 50  # the number of entries to display on the list view


myAdmin.add_view(MicroBlogModelView(User, db.session))
myAdmin.add_view(MicroBlogModelView(Post, db.session))

