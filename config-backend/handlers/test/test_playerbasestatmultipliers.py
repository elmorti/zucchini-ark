import unittest
from confighandlers.enums import CharacterStats
from confighandlers.playerbasestatmultipliers import ARKPlayerBaseStatMultipliers


class TestARKPlayerBaseStatMultipliers(unittest.TestCase):
    def setUp(self):

        self.test_config_string = 'PlayerBaseStatMultipliers[3]=1.0'

        self.test_config_dict = {
            'PlayerBaseStatMultipliers[3]': '1.0'
        }

        self.test_config = ARKPlayerBaseStatMultipliers()
        self.test_config.from_string(self.test_config_string)

    def tearDown(self):
        self.test_config = None

    def test_from_string(self):
        self.assertDictEqual(
            self.test_config._config_item,
            self.test_config_dict)

    def test_to_string(self):
        self.assertEqual(
            self.test_config.to_string(),
            self.test_config_string)


if __name__ == '__main__':
    unittest.main()
