import os


BASE_PATH = os.path.abspath(os.path.dirname(__file__))

''' 
     If the environment is not the default environment we change the class an make the import
    else we instantiate the correct configuration.
'''


def set_environment_instance(active_config, active_environment):
    _module = __import__(active_environment)
    _class = getattr(_module, active_config)
    return _class()


def get_environment(base_path):
    # Set the default configuration in case no config was set.
    active_environment = 'default'
    active_config = 'default.Config'
    # Get all environments in available
    for (dir_path, dir_name, filename) in os.walk(base_path):
        config_cls = filename[:-3]
        # Match the config file with the active environment.
        if config_cls == os.environ['ACTIVE_ENVIRONMENT']:
            active_config = "{}.{}Config".format(config_cls, config_cls.title)
            active_environment = config_cls
            break

    return active_config, active_environment


def bootstrap_configuration():
    environment = get_environment(BASE_PATH)
    return set_environment_instance(*environment)
