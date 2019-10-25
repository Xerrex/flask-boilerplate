"""Defines the flask app entry script.
"""

import os

from app import create_app

config = os.getenv('FLASK_CONFIG') or 'prod'
app = create_app(config)


if __name__ == '__main__':
    app.run()