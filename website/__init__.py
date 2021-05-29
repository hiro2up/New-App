from flask import Flask


#####################################################################
# The set up for the app
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'kadsbu209dn38h83nd d3jdo32' #keyphrase to secure the app


    from .views import views #importing routes from the views.py file
    from .auth import auth #importing routes from the auth.py file

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')


    return app