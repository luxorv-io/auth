from app import app


class Get(object):

    def __init__(self, route, **options):
        self.route = route
        self.options = options
        self.options['methods'] = [self.__class__.__name__.upper()]

    def __call__(self, func):
        print('{} CALLED'.format(self.options['methods'][0]))
        # Setting the endpoint name to the method name
        self.options['endpoint'] = func.__name__

        @app.route(self.route, **self.options)
        def get_wrapper(*args, **kwargs):
            # Call the method with the respective args
            return func(*args, **kwargs)
        return get_wrapper


class Post(object):

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

        # Append the route to the application
        @app.route(self.route, **self.options)
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
class Put(Post):
    pass


# Delete decorator
class Delete(Post):
    pass
