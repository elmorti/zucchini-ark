import unittest
from collections import OrderedDict
from confighandlers.dinoclassresistancemultipliers import ARKDinoClassResistanceMultipliers


class TestARKDinoClassResistanceMultipliers(unittest.TestCase):
    def setUp(self):

        self.test_config_string = ('DinoClassResistanceMultipliers=('
            'ClassName="MegaRex_Character_BP_C",'
            'Multiplier="0.1")'
            )

        self.test_config_dict =  OrderedDict(
            {'DinoClassResistanceMultipliers': OrderedDict(
                {
                    'ClassName': 'MegaRex_Character_BP_C',
                    'Multiplier': '0.1'
                })
            })

        self.test_config = ARKDinoClassResistanceMultipliers()
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
