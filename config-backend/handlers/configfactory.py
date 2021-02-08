import abc
import re
import importlib

import confighandlers
from collections import OrderedDict


def cleanup_string(text):
    """Removes quotes and parenthesis from the config string."""
    replace = re.compile(r'\"|\(|\)')
    return re.sub(replace, '', text)

class ARKConfigItemHandlerFactory(object):  
    def get_config_item(self, config_item_name):
        try:
            module = importlib.import_module('confighandlers.' + config_item_name.lower())
            class_ = getattr(module, 'ARK' + config_item_name)
            instance = class_()
            return instance
        except:
            instance = confighandlers.simpleconfigitem.ARKConfigSimple()
            return instance

class ARKConfigItemHandler(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def __init__(self):
        self._config_item = OrderedDict({'': None})
        self._config_name = next(iter(self._config_item))

    @property
    @abc.abstractmethod
    def config_name(self):
        return self._config_name

    @config_name.setter
    @abc.abstractmethod
    def config_name(self, value):
        raise AttributeError('Attribute is read_only')

    @property
    @abc.abstractmethod
    def config_item(self):
        return self._config_item
    
    @config_item.setter
    @abc.abstractmethod
    def config_item(self, config_item):
        self._config_item = config_item

    @config_item.deleter
    @abc.abstractmethod
    def config_item(self):
        self._config_item = OrderedDict()
        self._config_name = ''

    @abc.abstractmethod
    def from_string(self, config_string):
        raise NotImplementedError

    @abc.abstractmethod
    def to_string(self):
        raise NotImplementedError