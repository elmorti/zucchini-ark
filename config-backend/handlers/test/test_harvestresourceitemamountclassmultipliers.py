import unittest
from collections import OrderedDict
from confighandlers.harvestresourceitemamountclassmultipliers import ARKHarvestResourceItemAmountClassMultipliers


class TestARKHarvestResourceItemAmountClassMultipliers(unittest.TestCase):
    def setUp(self):

        self.test_config_string = (
            'HarvestResourceItemAmountClassMultipliers=('
                'ClassName="PrimalItemResource_Thatch_C",'
                'Multiplier="2.0"'
               ')'
            )

        self.test_config_dict = OrderedDict(
            {
                'HarvestResourceItemAmountClassMultipliers': OrderedDict(
                    {
                        'ClassName': 'PrimalItemResource_Thatch_C',
                        'Multiplier': '2.0'
                    })
            })

        self.test_config = ARKHarvestResourceItemAmountClassMultipliers()
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
