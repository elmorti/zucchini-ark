import unittest
from collections import OrderedDict
from confighandlers.overrideengramentries import ARKOverrideEngramEntries


class TestARKOverrideEngramEntries(unittest.TestCase):
    def setUp(self):

        self.test_config_string = (
            'OverrideEngramEntries=('
                'EngramIndex="1",'
                'EngramHidden="false",'
                'EngramPointsCost="3",'
                'EngramLevelRequirement="3",'
                'RemoveEngramPreReq="true"'
            ')'
        )

        self.test_config_dict = OrderedDict(
            {
                'OverrideEngramEntries': OrderedDict(
                    {
                        'EngramIndex': '1',
                        'EngramHidden': 'false',
                        'EngramPointsCost': '3',
                        'EngramLevelRequirement': '3',
                        'RemoveEngramPreReq': 'true'
                    })
            })

        self.test_config = ARKOverrideEngramEntries()
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
