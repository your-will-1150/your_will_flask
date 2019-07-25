import os

from app.main import create_app, db
from app import blueprint

application = create_app(os.getenv('FLASK_ENV'))
application.register_blueprint(blueprint)

application.app_context().push()
