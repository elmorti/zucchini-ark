import re
from collections import OrderedDict
from confighandlers.configfactory import ARKConfigItemHandler
from confighandlers.configfactory import cleanup_string



class ARKLevelExperienceRampOverrides(ARKConfigItemHandler):
    def __init__(self):
        super().__init__()
        self._config_item = OrderedDict(
            {'LevelExperienceRampOverrides': list()})
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
        levels = re.findall(
            r'ExperiencePointsForLevel\[[0-9]+\]=[0-9]+',
            config_string)
        for level in levels:
            lvl = re.search(r'[0-9]+$',level).group()
            self._config_item.get(self._config_name).append(lvl)

    def to_string(self, config_dict=None):
        if not config_dict:
            config_dict = self._config_item
        self._stack.append(self._config_name + '=(')
        for (idx, lvl) in enumerate(self._config_item.get(self._config_name)):
            self._stack.append(
                'ExperiencePointsForLevel[' + str(idx) + ']=' + lvl
            )
        self._stack.append(')')
        return ''.join(self._stack)