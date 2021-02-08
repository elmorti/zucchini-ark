import re
from collections import OrderedDict
from confighandlers.configfactory import ARKConfigItemHandler
from confighandlers.configfactory import cleanup_string


class ARKOverrideEngramEntries(ARKConfigItemHandler):
    def __init__(self):
        super().__init__()
        self._config_item = OrderedDict(
            {'OverrideEngramEntries': OrderedDict()})
        self._config_name = next(iter(self._config_item))
        self._stack = list()

    @property
    def config_item(self):
        return self._config_item
    
    @config_item.setter
    def config_item(self, config_item):
        super(self, config_item)
    
    @config_item.deleter
    def config_item(self):
        super(self)
    
    @property
    def config_name(self):
        super(self)
    
    @config_name.setter
    def config_name(self, value):
        super(self)

    def from_string(self, config_string):
        multiplier = OrderedDict()
        options = re.search(
            r'EngramIndex=.*$',
            config_string).group()

        for option in options.split(','):
            option = cleanup_string(option)
            multiplier.update(
                {k: v for k, v in [option.split('=')]}
            )
        self._config_item[self._config_name] = multiplier

    def to_string(self, config_item=None):
        if not config_item:
            config_item = self._config_item
        _items = len(config_item.items())
        for key, value in config_item.items():
            if isinstance(value, list):
                items = len(value)
                self._stack.append(key + '=(')
                for item in value:
                    self._stack.append('(') 
                    self.to_string(item)
                    self._stack.append(')')
                    items = items - 1
                    if items > 0:
                        self._stack.append(',')
                self._stack.append(')')

            elif isinstance(value, str):  # == str:
                # TODO(elmorti): add code to convert value type to int, float
                self._stack.append(key + '=' + '\"' + value + '\"')

            elif isinstance(value, dict):
                if key == self._config_name:
                    self._stack.append(key + '=(')
                else:
                    self._stack.append(key + '=')
                self.to_string(value)

            _items = _items - 1
            if _items > 0:
                self._stack.append(',')

        if key == self._config_name:
            self._stack.append(')')
        return ''.join(self._stack)