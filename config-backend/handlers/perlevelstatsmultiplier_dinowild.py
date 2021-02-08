import re
from collections import OrderedDict
from confighandlers.enums import CharacterStats
from confighandlers.configfactory import ARKConfigItemHandler
from confighandlers.configfactory import cleanup_string


# this might be good to make a singleton for all stats
class ARKPerLevelStatsMultiplier_DinoWild(ARKConfigItemHandler):
    def __init__(self):
        super().__init__()
        self._idx = '0'
        self._config_item = OrderedDict({
            'PerLevelStatsMultiplier_DinoWild[' + self._idx + ']': str()
        })
        self._config_name = next(iter(self._config_item))
        self._stack = list()

    @property
    def config_item(self):
        return self._config_item
    
    @config_item.setter
    def config_item(self, config_item):
        super(ARKPerLevelStatsMultiplier_DinoWild, config_item)
    
    @config_item.deleter
    def config_item(self):
        super(ARKPerLevelStatsMultiplier_DinoWild)
    
    @property
    def config_name(self):
        super(ARKPerLevelStatsMultiplier_DinoWild)
    
    @config_name.setter
    def config_name(self, value):
        super(ARKPerLevelStatsMultiplier_DinoWild, value)

    def to_string(self, config_dict=None):
        if not config_dict:
            config_dict = self._config_item
        return self._config_name + '=' + self._config_item.get(self._config_name)
    

    def from_string(self, config_string):
        self._idx = config_string.split(
            '=')[0].strip(
                'PerLevelStatsMultiplier_DinoWild').strip(
                    '[').strip(']')
        value = config_string.split('=')[1]
        self._config_item = OrderedDict({
            'PerLevelStatsMultiplier_DinoWild[' + self._idx + ']': value
        })
        self._config_name = next(iter(self._config_item))
