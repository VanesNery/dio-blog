
from flask import Flask
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from src.models.base import db

migrate = Migrate()
jwt = JWTManager()


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        SQLALCHEMY_DATABASE_URI='sqlite:///dio_blog.sqlite',
        JWT_SECRET_KEY='super-secret',
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_object('src.config')
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)


    # ensure the instance folder exists
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

    # register blueprints
    from src.controllers import user, post
    from src.controllers import auth
    from src.controllers import role

    app.register_blueprint(user.app)
    app.register_blueprint(post.app)
    app.register_blueprint(auth.app)
    app.register_blueprint(role.app)

    return app