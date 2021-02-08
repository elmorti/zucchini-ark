import unittest
from collections import OrderedDict
from confighandlers.simpleconfigitem import ARKConfigSimple


class TestARKConfigSimple(unittest.TestCase):
    def setUp(self):

        self.test_config_string = 'MaxTribeLogs="10"'
        self.test_config_dict = OrderedDict({'MaxTribeLogs': "10"})

        self.test_config = ARKConfigSimple()
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
