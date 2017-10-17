from importlib import import_module
from app.database import db

import inspect


def get_blueprint_or_base_app(func):
    module_name = func.__module__.split('.')[1]
    if module_name == 'app':
        module_name = ''
    _module = import_module('app.{}'.format(module_name))
    return getattr(_module, module_name)


def inject_session(func):
    def wrapper(obj, *args, **kwargs):
        return func(obj, db.session, *args, **kwargs)

    return wrapper


def import_all_subclasses_of(module_to_scan, base_cls, scope):
    """
    :param module_to_scan: Module to scan.
    :param baseclass: A base class to check.
    :param scope: globals(), locals() or a dict-like object.
    """
    for name, obj in inspect.getmembers(module_to_scan, inspect.isclass):
        if issubclass(obj, base_cls) and name != base_cls.__name__:
            scope[name] = obj
