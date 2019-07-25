import os

from app.main import create_app, db
from app import api

application = create_app(os.getenv('FLASK_ENV'))
application.register_blueprint(api)

application.app_context().push()


application.run()