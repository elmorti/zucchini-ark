import unittest
from collections import OrderedDict
from confighandlers.configoverridesupplycrateitems import ARKConfigOverrideSupplyCrateItems


class TestARKConfigOverrideSupplyCrateItems(unittest.TestCase):
    def setUp(self):

        self.test_config_string = 'ConfigOverrideSupplyCrateItems=(' \
            'SupplyCrateClassString="SupplyCrate_Level03_C",' \
            'MinItemSets="1",' \
            'MaxItemSets="1",' \
            'NumItemSetsPower="1.0",' \
            'bSetsRandomWithoutReplacement="true",' \
            'ItemSets=(' \
                '(' \
                    'MinNumItems="2",' \
                    'MaxNumItems="2",' \
                    'NumItemsPower="1.0",' \
                    'SetWeight="1.0",' \
                    'bItemsRandomWithoutReplacement="true",' \
                    'ItemEntries=(' \
                        '(' \
                            'EntryWeight="1.0",' \
                            'ItemClassStrings=("PrimalItemResource_Stone_C"),' \
                            'ItemsWeights=(1.0),' \
                            'MinQuantity="10.0",' \
                            'MaxQuantity="10.0",' \
                            'MinQuality="1.0",' \
                            'MaxQuality="1.0",' \
                            'bForceBlueprint="false",' \
                            'ChanceToBeBlueprintOverride="0.0"' \
                        '),' \
                        '(' \
                            'EntryWeight="1.0",' \
                            'ItemClassStrings=("PrimalItemResource_Thatch_C"),' \
                            'ItemsWeights=(1.0),' \
                            'MinQuantity="10.0",' \
                            'MaxQuantity="10.0",' \
                            'MinQuality="1.0",' \
                            'MaxQuality="1.0",' \
                            'bForceBlueprint="false",' \
                            'ChanceToBeBlueprintOverride="0.0"' \
                        ')' \
                    ')' \
                ')' \
            ')' \
        ')'

        self.test_config_item = OrderedDict(
            {'ConfigOverrideSupplyCrateItems': OrderedDict(
                {
                    'SupplyCrateClassString': 'SupplyCrate_Level03_C',
                    'MinItemSets': '1',
                    'MaxItemSets': '1',
                    'NumItemSetsPower': '1.0',
                    'bSetsRandomWithoutReplacement': 'true',
                    'ItemSets': [
                        OrderedDict(
                            {
                                'MinNumItems': '2',
                                'MaxNumItems': '2',
                                'NumItemsPower': '1.0',
                                'SetWeight': '1.0',
                                'bItemsRandomWithoutReplacement': 'true',
                                'ItemEntries': [
                                    OrderedDict(
                                        {
                                            'EntryWeight': '1.0',
                                            'ItemClassStrings': 'PrimalItemResource_Stone_C',
                                            'ItemsWeights': '1.0',
                                            'MinQuantity': '10.0',
                                            'MaxQuantity': '10.0',
                                            'MinQuality': '1.0',
                                            'MaxQuality': '1.0',
                                            'bForceBlueprint': 'false',
                                            'ChanceToBeBlueprintOverride': '0.0'
                                        }),
                                    OrderedDict(
                                        {
                                            'EntryWeight': '1.0',
                                            'ItemClassStrings': 'PrimalItemResource_Thatch_C',
                                            'ItemsWeights': '1.0',
                                            'MinQuantity': '10.0',
                                            'MaxQuantity': '10.0',
                                            'MinQuality': '1.0',
                                            'MaxQuality': '1.0',
                                            'bForceBlueprint': 'false',
                                            'ChanceToBeBlueprintOverride': '0.0'
                                        })
                                    ]
                                })
                            ]
                        })
                    })

        self.test_supply_crate_item_set = OrderedDict(
            {
                'MinNumItems': '2',
                'MaxNumItems': '2',
                'NumItemsPower': '1.0',
                'SetWeight': '1.0',
                'bItemsRandomWithoutReplacement': 'true',
                'ItemEntries': [
                    OrderedDict(
                        {
                            'EntryWeight': '1.0',
                            'ItemClassStrings': 'PrimalItemResource_Stone_C',
                            'ItemsWeights': '1.0',
                            'MinQuantity': '10.0',
                            'MaxQuantity': '10.0',
                            'MinQuality': '1.0',
                            'MaxQuality': '1.0',
                            'bForceBlueprint': 'false',
                            'ChanceToBeBlueprintOverride': '0.0'
                        }),
                    OrderedDict(
                        {
                            'EntryWeight': '1.0',
                            'ItemClassStrings': 'PrimalItemResource_Thatch_C',
                            'ItemsWeights': '1.0',
                            'MinQuantity': '10.0',
                            'MaxQuantity': '10.0',
                            'MinQuality': '1.0',
                            'MaxQuality': '1.0',
                            'bForceBlueprint': 'false',
                            'ChanceToBeBlueprintOverride': '0.0'
                        })
                    ]
                })

        self.test_supply_crate_item_entry = OrderedDict(
            {
                'EntryWeight': '1.0',
                'ItemClassStrings': 'PrimalItemResource_Stone_C',
                'ItemsWeights': '1.0',
                'MinQuantity': '10.0',
                'MaxQuantity': '10.0',
                'MinQuality': '1.0',
                'MaxQuality': '1.0',
                'bForceBlueprint': 'false',
                'ChanceToBeBlueprintOverride': '0.0'
            })

        self.test_config = ARKConfigOverrideSupplyCrateItems()
        self.test_config.from_string(self.test_config_string)
        self.test_item_set_index = 0

    def tearDown(self):
        self.test_config = None
    
    def test_add_item_set(self):
        self.test_config.add_item_set(self.test_supply_crate_item_set)
        supply_crate = self.test_config_item.get('ConfigOverrideSupplyCrateItems')
        supply_crate.get('ItemSets').append(self.test_supply_crate_item_set)
        self.assertDictEqual(self.test_config.config_item, self.test_config_item)

    def test_add_item_entry(self):
        self.test_config.add_item_entry(
            self.test_item_set_index,
            self.test_add_item_entry)
        supply_crate = self.test_config_item.get('ConfigOverrideSupplyCrateItems')
        item_set = supply_crate.get('ItemSets')[self.test_item_set_index]
        item_set.get('ItemEntries').append(self.test_add_item_entry)
        self.assertDictEqual(self.test_config.config_item, self.test_config_item)

    def test_del_item_entry(self):
        self.test_config.del_item_entry(
            self.test_item_set_index,
            'PrimalItemResource_Stone_C')
        supply_crate = self.test_config_item.get('ConfigOverrideSupplyCrateItems')
        entries = supply_crate.get('ItemSets')[self.test_item_set_index].get('ItemEntries')
        for entry in entries:
            if 'PrimalItemResource_Stone_C' in entry.values():
                del(entry)

        self.assertDictEqual(self.test_config.config_item, self.test_config_item)

    def test_del_item_set(self):
        self.test_config.del_item_set(self.test_item_set_index)
        supply_crate = self.test_config_item.get('ConfigOverrideSupplyCrateItems')
        del(supply_crate.get('ItemSets')[0])
        self.assertDictEqual(self.test_config.config_item, self.test_config_item)
    
    def test_from_string(self):
        self.assertDictEqual(
            self.test_config.config_item,
            self.test_config_item)

    def test_to_string(self):
        self.assertEqual(
            self.test_config.to_string(),
            self.test_config_string)


if __name__ == '__main__':
    unittest.main()
