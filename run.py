import os

from flask import Flask

from api.api_blueprint import api_bp
from api.common import ma, db


def create_app():
    app = Flask(__name__)
    app.config.from_object(os.environ['APP_SETTINGS'])
    app.register_blueprint(api_bp)
    db.init_app(app)
    ma.init_app(app)
    with app.app_context():
        db.create_all()
    return app


port = int(os.environ.get("PORT", 5000))
app = create_app()
app.run(port=port)
