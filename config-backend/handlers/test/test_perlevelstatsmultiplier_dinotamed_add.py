import unittest
from confighandlers.enums import CharacterStats
from confighandlers.perlevelstatsmultiplier_dinotamed_add import ARKPerLevelStatsMultiplier_DinoTamed_Add


class TestARKPerLevelStatsMultiplier_DinoTamed_Add(unittest.TestCase):
    def setUp(self):

        self.test_config_string = 'PerLevelStatsMultiplier_DinoTamed_Add[3]=1.0'

        self.test_config_dict = {
            'PerLevelStatsMultiplier_DinoTamed_Add[3]': '1.0'
        }

        self.test_config = ARKPerLevelStatsMultiplier_DinoTamed_Add()
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