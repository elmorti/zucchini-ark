import configparser
import confighandlers
import re
from configparsers.arkparser import ARKParser

class ARKIniParser(ARKParser):
    def __init__(self, config_file_name, config_section):
        self._config_handlers = list()
        self._config_file_name = config_file_name
        self._config_section = config_section
        self._parser = configparser.RawConfigParser()
        self._parser.optionxform = str

    def load_config(self):
        with open(self._config_file_name, 'r') as config_file:
            self._parser.read_file(config_file)
        
        items = self._parser.items(self._config_section)

        for item in items:
            config_item_name = re.sub(r'\[[0-9]+\]','',item[0])
            handler = confighandlers.configfactory.ARKConfigItemHandlerFactory().get_config_item(config_item_name)
            handler.from_string('='.join(item))
            self._config_handlers.append(handler)

    def save_config(self):
        self._parser.remove_section(self.config_section)
        self._parser.add_section(self.config_section)
        for handler in self._config_handlers:
            option = handler.to_string().split('=')[0]
            value = handler.to_string().split('=')[1]
            self._parser.set(self._config_section, option, value)
        with open('test.ini', 'w+') as configfile:
            self._parser.write(configfile)

    @property
    def config_handlers(self):
        return self._config_handlers
    
    @config_handlers.setter
    def config_handlers(self, value):
        super(self)

    @config_handlers.deleter
    def config_handlers(self, value):
        super(self)

    @property
    def config_file_name(self):
        super(self)
    
    @config_file_name.setter
    def config_file_name(self, config_item):
        super(self)

    @config_file_name.deleter
    def config_file_name(self):
        super(self)

    @property
    def config_section(self):
        return self._config_section
    
    @config_section.setter
    def config_section(self, value):
        super(self)
    
    @config_section.deleter
    def config_section(self, value):
        super(self)

    def from_string(self, config_string):
        super(self)

    def to_string(self):
        super(self)