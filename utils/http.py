from importlib import import_module
from utils import get_blueprint_or_base_app


class get(object):

    def __init__(self, route, **options):
        self.route = route
        self.options = options
        self.options['methods'] = [self.__class__.__name__.upper()]

    def __call__(self, func):
        print(func.__module__)
        print('{} CALLED'.format(self.options['methods'][0]))
        # Setting the endpoint name to the method name
        self.options['endpoint'] = func.__name__

        _app = get_blueprint_or_base_app(func)

        @_app.route(self.route, **self.options)
        def get_wrapper(*args, **kwargs):
            # Call the method with the respective args
            return func(*args, **kwargs)
        return get_wrapper


class post(object):

    def __init__(self, route, body=None, endpoint=None, **options):
        self.route = route
        self._body = body
        self.endpoint = endpoint
        self.options = options
        self.options['methods'] = [self.__class__.__name__.upper()]

    def __call__(self, func):
        print('{} CALLED'.format(self.options['methods'][0]))
        print(self._body.__name__)
        # Setting the endpoint name to the resource_name-method_name
        self.options.setdefault('endpoint', "{}-{}".format(self.endpoint, func.__name__))

        _app = get_blueprint_or_base_app(func)

        # Append the route to the application
        @_app.route(self.route, **self.options)
        def get_wrapper(**kwargs):
            from flask import request
            # append request body to the method
            self.get_body(request.get_json(), kwargs)
            # Call the method with the respective args
            return func(**kwargs)
        return get_wrapper

    def get_body(self, json, kwargs):
        if self._body is not None:
            kwargs.setdefault(
                self._body.__name__.lower(),
                self._body(**json)
            )


# Put decorator
class put(post):
    pass


# Delete decorator
class delete(post):
    pass
