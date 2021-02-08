import unittest
from collections import OrderedDict
from confighandlers.overridenamedengramentries import ARKOverrideNamedEngramEntries


class TestARKOverrideNamedEngramEntries(unittest.TestCase):
    def setUp(self):

        self.test_config_string = (
            'OverrideNamedEngramEntries=('
                'EngramClassName="EngramEntry_StoneHatchet_C",'
                'EngramHidden="false",'
                'EngramPointsCost="3",'
                'EngramLevelRequirement="3",'
                'RemoveEngramPreReq="true"'
                ')'
        )

        self.test_config_dict = OrderedDict(
            {
                'OverrideNamedEngramEntries': OrderedDict(
                    {
                        'EngramClassName': 'EngramEntry_StoneHatchet_C',
                        'EngramHidden': 'false',
                        'EngramPointsCost': '3',
                        'EngramLevelRequirement': '3',
                        'RemoveEngramPreReq': 'true'
                    })
            })

        self.test_config = ARKOverrideNamedEngramEntries()
        self.test_config.from_string(self.test_config_string)

    def tearDown(self):
        self.test_config = None

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
