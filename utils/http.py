from utils import get_blueprint_or_base_app, get_service
from flask import request


class BaseHttpDecorator(object):
    def inject_body(self, json, kwargs):
        if self._body is not None:
            kwargs.setdefault(
                self._body.__name__.lower(),
                self._body(**json)
            )

    def inject_service(self, func, kwargs):
        _service = get_service(func)
        kwargs.setdefault('service', _service())


class get(BaseHttpDecorator):
    def __init__(self, route, **options):
        self.route = route
        self.options = options
        self.options['methods'] = [self.__class__.__name__.upper()]

    def __call__(self, func):
        # Getting the right app name to set the routing
        _app, name = get_blueprint_or_base_app(func)

        # Setting the endpoint name to the method name

        self.options.setdefault(
            'endpoint',
            "{}-{}".format(name, func.__name__)
        )

        @_app.route(self.route, **self.options)
        def get_wrapper(**kwargs):
            self.inject_service(func, kwargs)
            # Call the method with the respective args
            return func(**kwargs)

        return get_wrapper


class post(BaseHttpDecorator):
    def __init__(self, route, body=None, **options):
        self.route = route
        self._body = body
        self.options = options
        self.options['methods'] = [self.__class__.__name__.upper()]

    def __call__(self, func):
        # Getting the right app name to set the routing
        _app, name = get_blueprint_or_base_app(func)

        # Setting the endpoint name to the method name

        self.options.setdefault(
            'endpoint',
            "{}-{}".format(name, func.__name__)
        )

        # Append the route to the application
        @_app.route(self.route, **self.options)
        def get_wrapper(**kwargs):
            # Append request body to the method
            self.inject_body(request.get_json(), kwargs)
            self.inject_service(func, kwargs)
            # Call the method with the respective args
            return func(**kwargs)
        return get_wrapper


# Put decorator
class put(post):
    pass


# Delete decorator
class delete(post):
    pass
