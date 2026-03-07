# Flask is a main class that creates your web application/ API application.
# Object of Flask class is our WSGI application. Flask constructor takes the name of current module (__name__) as argument.


from flask import Flask
from app.routes.sales_routes import sales_blueprint

def create_app():
    app = Flask(__name__)
    app.register_blueprint(sales_blueprint)
    return app
