import abc
from collections import OrderedDict

class ARKParserFactory(object):  
    def get_config_item(self, config_item_name, config_section):
        _classname = 'ARK' + config_item_name
        if _classname in globals().keys():
            return _classname(config_item_name, config_section)
        else:
            raise ValueError('Config Item not found or implemented %s', config_item_name)

class ARKParser(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def __init__(self, config_item_name, config_section):
        self._config_handlers = list()
        self._config_file_name = str()
        self._config_section = str()

    @abc.abstractmethod
    def load_config(self, config_file_name, config_section=None):
        raise NotImplementedError
    
    @abc.abstractmethod
    def save_config(self, config_file_name, config_section=None):
        raise NotImplementedError

    @property
    @abc.abstractproperty
    def config_handlers(self):
        return self._config_handlers
    
    @config_handlers.setter
    @abc.abstractproperty
    def config_handlers(self, value):
        raise NotImplementedError('Property setter not implemented.')
    
    @config_handlers.deleter
    @abc.abstractproperty
    def config_handlers(self, value):
        raise NotImplementedError('Property setter not implemented.')

    @property
    @abc.abstractproperty
    def config_file_name(self):
        return self._config_file_name
    
    @config_file_name.setter
    @abc.abstractmethod
    def config_file_name(self, config_item):
        raise AttributeError('Property is read only.')

    @config_file_name.deleter
    @abc.abstractmethod
    def config_file_name(self):
        raise AttributeError('Property is read only.')

    @property
    @abc.abstractproperty
    def config_section(self):
        return self._config_section
    
    @config_section.setter
    @abc.abstractproperty
    def config_section(self, value):
        raise NotImplementedError('Property setter not implemented.')
    
    @config_section.deleter
    @abc.abstractproperty
    def config_section(self, value):
        raise NotImplementedError('Property setter not implemented.')

    @abc.abstractmethod
    def from_string(self, config_string):
        raise NotImplementedError

    @abc.abstractmethod
    def to_string(self):
        raise NotImplementedError