from flask import Flask, Blueprint
from .extensions import mysql
from .login import login
from .register import register
from .forgot import forgot
from .logout import logout
from .admin import main
from .product import product
from .supplier import supplier
from .profile import profile
from .member import member
from .report import report
def create_app():
    app = Flask(__name__)

    app.config['MYSQL_HOST'] = 'localhost'
    app.config['MYSQL_USER'] = 'root'
    app.config['MYSQL_PASSWORD'] = 'qwebnm123'
    app.config['MYSQL_DB'] = 'umbrellapos'
    #app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

    mysql.init_app(app)

    app.secret_key = "Arm#$1rfaklsapP()!@"
    
    app.register_blueprint(main)
    app.register_blueprint(login)
    app.register_blueprint(register)
    app.register_blueprint(forgot)
    app.register_blueprint(logout)
    app.register_blueprint(product)
    app.register_blueprint(supplier)
    app.register_blueprint(profile)
    app.register_blueprint(member)
    app.register_blueprint(report)

    return app
