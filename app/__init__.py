"""File defines the Flask app creation methods.
"""

from flask import Flask

from config import config_envs


def create_app(config):
    """Create a Flask app instance.
    
    Arguments:
        config {String} -- name of configuration environment
    
    Returns:
        Flask -- Instance of Flask app
    """

    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config_envs[config])

    @app.route('/')
    def hello_world():
        return 'welcome to snakeeyes'


    return app