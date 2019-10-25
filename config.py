"""File contains app configuratins objects.
"""


import os


class BaseConfigs:
    """Defines common app configurations.
    """
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'provide a more complex secret key'


class DevelopmentConfigs(BaseConfigs):
    """Defines Development specific 
    configurations.
    """
    DEBUG = True


class ProductionConfigs(BaseConfigs):
    """Defines Production configurations for the app.
    """
    pass


class TestingConfigs(BaseConfigs):
    """Defines Testing configurations for the app.
    """
    TESTING = True


config_envs = {
    "Dev": DevelopmentConfigs,
    "Prod": ProductionConfigs,
    "Testing": TestingConfigs
}
