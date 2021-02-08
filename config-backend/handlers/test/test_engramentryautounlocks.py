import unittest
from collections import OrderedDict
from confighandlers.engramentryautounlocks import ARKEngramEntryAutoUnlocks


class TestARKEngramEntryAutoUnlocks(unittest.TestCase):
    def setUp(self):

        self.test_config_string = ('EngramEntryAutoUnlocks=('
            'EngramClassName="EngramEntry_TekTeleporter_C",'
            'LevelToAutoUnlock="0"'
        ')'
        )

        self.test_config_dict = OrderedDict(
            {
                'EngramEntryAutoUnlocks': OrderedDict(
                    {
                    'EngramClassName': 'EngramEntry_TekTeleporter_C', 
                    'LevelToAutoUnlock': '0'
                    })
            })

        self.test_config = ARKEngramEntryAutoUnlocks()
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