import re
from collections import OrderedDict
from confighandlers.configfactory import ARKConfigItemHandler
from confighandlers.configfactory import cleanup_string


class ARKConfigOverrideItemCraftingCosts(ARKConfigItemHandler):
    """Handler for ConfigAddNPCSpawnEntriesContainer setting

        Handles one ConfigAddNPCSpawnEntriesContainer, per documentation this
        option can be repeated once per container (TO BE TESTED).

        Properties:
            self._config_item = OrderedDict containing the configuration options
            and Lists of OrderedDicts for setting up spawns.
            self._config_name = Read only contains only the config name
            self._stack = Used internally to return the string version of
            self._config_item

        Methods:
            add_spawn_entry
            add_spawn_limit
            del_spawn_entry
            del_spawn_limit
            from_string
            to_string
    """

    def __init__(self):
        super().__init__()
        self._config_item = OrderedDict(
            {'ConfigOverrideItemCraftingCosts': list()})
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
    
    def add_crafting_requirement(self, resource_requirement):
        self._config_item.get(self.config_name).get(
            'BaseCraftingResourceRequirements'
        ).append(resource_requirement)
    
    def del_crafting_requirement(self, requirement_name):
        requirements = self._config_item.get(self.config_name).get(
            'BaseCraftingResourceRequirements')
        for requirement in requirements:
            if requirement.get('ResourceItemTypeString') == requirement_name:
                requirements.remove(requirement)

    def from_string(self, config_string):
        item_class_name = re.search(
            r'ItemClassString=\"\w+\"',config_string).group()

        item_class = OrderedDict()
        item_class_name = cleanup_string(item_class_name)
        item_class.update(
            {k: v for k, v in [item_class_name.split('=')]}
        )

        item_class.update({'BaseCraftingResourceRequirements': list()})

        for resource_item in re.findall(
            r'ResourceItemTypeString=.*?' \
            r'(?=\),)' \
            r'|ResourceItemTypeString.*$',config_string):
            
            parsed_options = OrderedDict()
            for option in resource_item.split(','):
                option = cleanup_string(option)
                parsed_options.update(
                    {k: v for k, v in [option.split('=')]}
                )
            
            item_class['BaseCraftingResourceRequirements'].append(
                parsed_options)
        self._config_item[self._config_name] = item_class
                
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