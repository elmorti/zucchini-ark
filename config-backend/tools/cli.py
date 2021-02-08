import pprint
from configparsers import arkiniparser

def get_option(handlers, option_name):
    for handler in handlers:
        if option_name in handler.config_item:
            return handler

def main():
    serversettings = arkiniparser.ARKIniParser('Game.ini','/script/shootergame.shootergamemode')
    serversettings.load_config()
    harvest = get_option(serversettings.config_handlers, 'ConfigOverrideSupplyCrateItems')
    #harvest.from_string('HarvestHealthMultiplier=666')
    #print(harvest.to_string())
    #pprint.pprint(harvest.config_item.get('ConfigOverrideSupplyCrateItems'))
    #serversettings.save_config()
    harvest.config_name = 'adadsds'
    print(harvest.config_name)

if __name__ == "__main__":
    main()