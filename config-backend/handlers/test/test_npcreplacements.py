import unittest
from collections import OrderedDict
from confighandlers.npcreplacements import ARKNPCReplacements


class TestARKNPCReplacements(unittest.TestCase):
    def setUp(self):

        self.test_config_string = ('NPCReplacements=('
            'FromClassName="MegaRaptor_Character_BP_C",'
            'ToClassName="Dodo_Character_BP_C"'
        ')'
        )

        self.test_config_dict = OrderedDict(
            {
                'NPCReplacements': OrderedDict(
                    {
                        'FromClassName': 'MegaRaptor_Character_BP_C', 
                        'ToClassName': 'Dodo_Character_BP_C'
                    })
            })

        self.test_config = ARKNPCReplacements()
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
