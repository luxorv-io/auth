from importlib import import_module

import os

BASE_PATH = os.path.abspath(os.path.dirname(__file__))

''' 
     If the environment is not the default environment we change the class an make the import
    else we instantiate the correct configuration.
'''


def bootstrap_configuration():
    # TODO: change prints with logging
    print("Bootstraping the configuration with the {} environment".format(os.environ['ACTIVE_ENVIRONMENT']))
    # Selected environment
    selected_environment = os.environ['ACTIVE_ENVIRONMENT']

    # Set the environment module depending on the selected environment type
    active_config = "{}Config".format(selected_environment.title())
    active_environment = 'config.{}'.format(selected_environment)
    print("Pulling up the {} class from {}".format(active_config, active_environment))
    # Import module and instantiate class
    _module = import_module(active_environment)
    _class = getattr(_module, active_config)

    return _class()
