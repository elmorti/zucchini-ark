import re
from collections import OrderedDict
from confighandlers.configfactory import ARKConfigItemHandler
from confighandlers.configfactory import cleanup_string


class ARKConfigSimple(ARKConfigItemHandler):
    def __init__(self):
        super().__init__()
        self._config_item = OrderedDict()
        self._stack = list()

    @property
    def config_item(self):
        return self._config_item
    
    @config_item.setter
    def config_item(self, config_item):
        super(ARKConfigSimple, config_item)
    
    @config_item.deleter
    def config_item(self):
        super(ARKConfigSimple)
    
    @property
    def config_name(self):
        super(ARKConfigSimple)
    
    @config_name.setter
    def config_name(self, value):
        super(ARKConfigSimple, value)

    def from_string(self, config_string=None):
        if not config_string:
            config_string = self._config_item
        _replace = re.compile(r'\"|\(|\)')
        k,v = re.sub(_replace, '', config_string).split('=')
        self._config_name = k
        self._config_item.update([(k,v)])

    def to_string(self):
        return self._config_name + '=' \
        + '\"' + self._config_item.get(self._config_name) + '\"'