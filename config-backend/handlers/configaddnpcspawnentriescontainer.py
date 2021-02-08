import re
from collections import OrderedDict
from confighandlers.configfactory import ARKConfigItemHandler
from confighandlers.configfactory import cleanup_string


class ARKConfigAddNPCSpawnEntriesContainer(ARKConfigItemHandler):
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
            {'ConfigAddNPCSpawnEntriesContainer': list()})
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

    def add_spawn_entry(self, container_name, entry):
        container = self._config_item.get(self._config_name)
        if container.get('NPCSpawnEntriesContainerClassString') == container_name:
            container.get('NPCSpawnEntries').append(entry)

    def add_spawn_limit(self, container_name, limit):
        container = self._config_item.get(self._config_name)
        if container.get('NPCSpawnEntriesContainerClassString') == container_name:
            container.get('NPCSpawnLimits').append(limit)

    def del_spawn_entry(self, container_name, entry_name):
        container = self._config_item.get(self._config_name)
        if container.get('NPCSpawnEntriesContainerClassString') == container_name:
            entries = container.get('NPCSpawnEntries')
            for entry in entries:
                if entry.get('AnEntryName') == entry_name:
                    entries.remove(entry)

    def del_spawn_limit(self, container_name, spawn_limit):
        container = self._config_item[self._config_name]
        if container.get('NPCSpawnEntriesContainerClassString') == container_name:
            entries = container.get('NPCSpawnLimits')
            for entry in entries:
                if entry.get('NPCClassString') == spawn_limit:
                    entries.remove(entry)

    def from_string(self, config_string):
        container_name = re.search(
            r'NPCSpawnEntriesContainerClassString\=\"\w+\"',
            config_string).group()

        spawn_class = OrderedDict()
        container_name = cleanup_string(container_name)
        spawn_class.update(
            {k: v for k, v in [container_name.split('=')]}
            )
        spawn_class.update({'NPCSpawnEntries': list()})
        spawn_class.update({'NPCSpawnLimits': list()})

        spawn_entries = re.findall(
            r'NPCSpawnEntries=.*?'
            r'(?=,NPCSpawnLimits)',
            config_string)

        for spawn_entry in spawn_entries:
            entry_names = re.findall(
                r'AnEntryName=.*?'
                r'(?=,\(AnEntryName)'
                r'|AnEntryName=.*$',
                spawn_entry)

            for options in entry_names:
                parsed_options = OrderedDict()
                for option in options.split(','):
                    option = cleanup_string(option)
                    parsed_options.update(
                        {k: v for k, v in [option.split('=')]}
                    )
                spawn_class.get('NPCSpawnEntries').append(parsed_options)

        spawn_limits = re.findall(
            r'NPCSpawnLimits=.*?'
            r'(?=,NPCSpawnEntriesContainerClassString)'
            r'|NPCSpawnLimits.*$',
            config_string)

        for spawn_limit in spawn_limits:
            spawn_limits_options = re.findall(
                r'NPCClassString=.*?'
                r'(?=,\(NPCClassString)'
                r'|NPCClassString=.*$',
                spawn_limit)

            for options in spawn_limits_options:
                parsed_options = OrderedDict()
                for option in options.split(','):
                    option = cleanup_string(option)
                    parsed_options.update(
                        {k: v for k, v in [option.split('=')]}
                    )
                spawn_class.get('NPCSpawnLimits').append(parsed_options)
        self._config_item[self._config_name] = spawn_class

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
                if key == 'NPCsToSpawnStrings':
                    self._stack.append(key + '=' + '(\"' + value + '\")')
                else:
                    self._stack.append(key + '=' + '\"' + value + '\"')

            elif isinstance(value, dict):
                if key == 'ConfigAddNPCSpawnEntriesContainer':
                    self._stack.append(key + '=(')
                else:
                    self._stack.append(key + '=')
                self.to_string(value)

            _items = _items - 1
            if _items > 0:
                self._stack.append(',')

        if key == 'ConfigAddNPCSpawnEntriesContainer':
            self._stack.append(')')
        return ''.join(self._stack)
