from flask import Flask, session
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

import config

db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    # ORM
    db.init_app(app)
    migrate.init_app(app, db)

    from . import models

    # 블루프린트
    from .views import main_views, upload_views, auth_views, admin_views
    app.register_blueprint(main_views.bp)
    app.register_blueprint(upload_views.bp)
    app.register_blueprint(auth_views.bp)
    app.register_blueprint(admin_views.bp)

    from yp.plotlydash.dashboard import create_dashboard
    app = create_dashboard(app)

    return app

