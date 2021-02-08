import unittest
from collections import OrderedDict
from confighandlers.levelexperiencerampoverrides import ARKLevelExperienceRampOverrides


class TestARKLevelExperienceRampOverrides(unittest.TestCase):
    def setUp(self):

        self.test_config_string = ('LevelExperienceRampOverrides=('
            'ExperiencePointsForLevel[0]=1'
        ')')

        self.test_config_dict = OrderedDict(
            {
                'LevelExperienceRampOverrides': ['1']
            })

        self.test_config = ARKLevelExperienceRampOverrides()
        self.test_config.from_string(self.test_config_string)

    def tearDown(self):
        self.test_config = None

    def test_from_string(self):
        self.assertDictEqual(
            self.test_config.config_item,
            self.test_config_dict)

    def test_to_string(self):
        self.assertEqual(
            self.test_config.to_string(),
            self.test_config_string)


if __name__ == '__main__':
    unittest.main()
