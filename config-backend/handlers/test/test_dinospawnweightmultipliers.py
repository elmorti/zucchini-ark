import unittest
from confighandlers.dinospawnweightmultipliers import ARKDinoSpawnWeightMultipliers


class TestARKDinoSpawnWeightMultipliers(unittest.TestCase):
    def setUp(self):

        self.canon_config_string = 'DinoSpawnWeightMultipliers=(' \
            'DinoNameTag="Bronto",' \
            'SpawnWeightMultiplier="10.0",' \
            'OverrideSpawnLimitPercentage="true",' \
            'SpawnLimitPercentage="0.5"' \
        ')'

        self.canon_config_dict = {'DinoSpawnWeightMultipliers': {
            'DinoNameTag': 'Bronto',
            'SpawnWeightMultiplier': '10.0',
            'OverrideSpawnLimitPercentage': 'true',
            'SpawnLimitPercentage': '0.5'
            }
        }

        self.test_config = ARKDinoSpawnWeightMultipliers()
        self.test_config.from_string(self.canon_config_string)

    def tearDown(self):
        self.test_config = None

    def test_from_string(self):
        self.assertDictEqual(
            self.test_config.config_item,
            self.canon_config_dict)

    def test_to_string(self):
        self.assertEqual(
            self.test_config.to_string(self.canon_config_dict),
            self.canon_config_string)


if __name__ == '__main__':
    unittest.main()
