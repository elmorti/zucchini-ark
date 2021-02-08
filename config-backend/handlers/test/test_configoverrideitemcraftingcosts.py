import unittest
from collections import OrderedDict
from confighandlers.configoverrideitemcraftingcosts import ARKConfigOverrideItemCraftingCosts


class TestARKConfigOverrideItemCraftingCosts(unittest.TestCase):
    def setUp(self):

        self.test_config_string = 'ConfigOverrideItemCraftingCosts=(' \
            'ItemClassString="PrimalItem_WeaponStoneHatchet_C",' \
            'BaseCraftingResourceRequirements=(' \
                '(' \
                    'ResourceItemTypeString="PrimalItemResource_Thatch_C",' \
                    'BaseResourceRequirement="1.0",' \
                    'bCraftingRequireExactResourceType="false"' \
                '),' \
                '(' \
                    'ResourceItemTypeString="PrimalItemAmmo_ArrowStone_C",'\
                    'BaseResourceRequirement="2.0",' \
                    'bCraftingRequireExactResourceType="false"' \
                ')' \
            ')' \
        ')'

        self.test_config_dict = OrderedDict({
            'ConfigOverrideItemCraftingCosts': 
            OrderedDict({
                'ItemClassString': 'PrimalItem_WeaponStoneHatchet_C',
                'BaseCraftingResourceRequirements': [
                    OrderedDict({
                        'ResourceItemTypeString': 'PrimalItemResource_Thatch_C',
                        'BaseResourceRequirement': '1.0',
                        'bCraftingRequireExactResourceType': 'false'
                    }),
                    OrderedDict({
                        'ResourceItemTypeString': 'PrimalItemAmmo_ArrowStone_C',
                        'BaseResourceRequirement': '2.0',
                        'bCraftingRequireExactResourceType': 'false'
                    })
                ]
            })
        })

        self.test_config = ARKConfigOverrideItemCraftingCosts()
        self.test_config.from_string(self.test_config_string)

    def tearDown(self):
        self.test_config = None

    def test_add_crafting_requirements(self):
        pass
    
    def test_del_crafting_requirements(self):
        pass
        
    def test_from_string(self):
        self.assertDictEqual(
            self.test_config.config_item,
            self.test_config_dict)

    def test_to_string(self):
        self.assertEqual(
            self.test_config.to_string(self.test_config_dict),
            self.test_config_string)


if __name__ == '__main__':
    unittest.main()
