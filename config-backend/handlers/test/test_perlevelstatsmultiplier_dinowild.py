import unittest
from confighandlers.enums import CharacterStats
from confighandlers.perlevelstatsmultiplier_dinowild import ARKPerLevelStatsMultiplier_DinoWild


class TestARKPerLevelStatsMultiplier_DinoWild(unittest.TestCase):
    def setUp(self):

        self.test_config_string = 'PerLevelStatsMultiplier_DinoWild[3]=1.0'

        self.test_config_dict = {
            'PerLevelStatsMultiplier_DinoWild[3]': '1.0'
        }

        self.test_config = ARKPerLevelStatsMultiplier_DinoWild()
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
