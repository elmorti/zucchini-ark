import re
from collections import OrderedDict
from confighandlers.configfactory import ARKConfigItemHandler
from confighandlers.configfactory import cleanup_string


class ARKConfigOverrideSupplyCrateItems(ARKConfigItemHandler):
    """
        TODO(elmorti): Class summary
    """

    def __init__(self):
        super().__init__()
        self._config_name = 'ConfigOverrideSupplyCrateItems'
        self._config_item = OrderedDict(
            {self._config_name: list()})
        self._stack = list()

    @property
    def config_item(self):
        return super().config_item
    
    @config_item.setter
    def config_item(self, config_item):
        super().config_item(config_item)
    
    @config_item.deleter
    def config_item(self):
        super().config_item
    
    @property
    def config_name(self):
        return super().config_name
    
    @config_name.setter
    def config_name(self, value):
        super().config_name

    def add_item_set(self, item_set):
        supply_crate = self._config_item.get(self._config_name)
        supply_crate.get('ItemSets').append(item_set)

    def add_item_entry(self, item_set_index, item_entry):
        supply_crate = self._config_item.get(self._config_name)
        supply_crate.get('ItemSets')[item_set_index].get('ItemEntries').append(item_entry)

    def del_item_set(self, item_set_index):
        supply_crate = self._config_item.get(self._config_name)
        del(supply_crate.get('ItemSets')[item_set_index])

    def del_item_entry(self, item_set_index, item_name):
        supply_crate = self._config_item.get(self._config_name)
        item_set = supply_crate.get('ItemSets')[item_set_index]
        for item in item_set.get('ItemEntries'):
            if item_name in item.values():
                del(item)

    def from_string(self, config_string):
        supply_crate_name = re.search(
            r'SupplyCrateClassString=\"\w+\"',
            config_string).group()

        supply_crate = OrderedDict()
        supply_crate_name = cleanup_string(supply_crate_name)
        supply_crate.update(
            {k: v for k, v in [supply_crate_name.split('=')]}
        )

        supply_crate_options = re.search(
            r'MinItemSets.*?(?=,ItemSets)',
            config_string).group().split(',')
        
        for option in supply_crate_options:
            option = cleanup_string(option)
            supply_crate.update(
                {k: v for k, v in [option.split('=')]}
            )

        supply_crate.update({'ItemSets': list()})

        item_sets = re.findall(
            r'MinNumItems=.*?(?=,MinNumItems)|MinNumItems=.*',
            config_string)
        for item_set in item_sets:
            item_set_dict = OrderedDict()
            item_set_options = re.search(
                r'MinNumItems.*?(?=\,ItemEntries)',
                item_set).group().split(',')
            for option in item_set_options:
                option = cleanup_string(option)
                item_set_dict.update(
                    {k: v for k, v in [option.split('=')]}
                )
            
            item_entries  = re.findall(
                r'EntryWeight=.*?(?=,\(EntryWeight)|EntryWeight=.*',
                re.search(
                    r'ItemEntries=\(.*\)\)'
                    ,item_set).group())

            item_set_dict.update({'ItemEntries': list()})
            
            for item_entry in item_entries:
                options = OrderedDict()
                for option in item_entry.split(','):
                    option = cleanup_string(option)
                    options.update(
                        {k: v for k, v in [option.split('=')]}
                    )
                item_set_dict.get('ItemEntries').append(options)
            supply_crate.get('ItemSets').append(item_set_dict)
        self._config_item[self._config_name] = supply_crate


    def to_string(self, config_dict=None):
        if not config_dict:
            config_dict = self._config_item
        _items = len(config_dict.items())
        for key, value in config_dict.items():
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
                if key == 'ItemClassStrings':
                    self._stack.append(key + '=' + '(\"' + value + '\")')
                elif key == 'ItemsWeights':
                    self._stack.append(key + '=' + '(' + value + ')')
                else:
                    self._stack.append(key + '=' + '\"' + value + '\"')

            elif isinstance(value, dict):
                if key is self._config_name:
                    self._stack.append(key + '=(')
                else:
                    self._stack.append(key + '=')
                self.to_string(value)

            _items = _items - 1
            if _items > 0:
                self._stack.append(',')

        if key is self._config_name:
            self._stack.append(')')
        return ''.join(self._stack)