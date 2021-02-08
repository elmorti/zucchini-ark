import unittest
from collections import OrderedDict
from confighandlers.configsubtractnpcspawnentriescontainer import ARKConfigSubtractNPCSpawnEntriesContainer


class TestARKConfigSubtractNPCSpawnEntriesContainer(unittest.TestCase):
    def setUp(self):
        self.test_config_string = 'ConfigSubtractNPCSpawnEntriesContainer=(' \
            'NPCSpawnEntriesContainerClassString="DinoSpawnEntriesBeach_C",' \
            'NPCSpawnEntries=(' \
                '(NPCsToSpawnStrings=("Trike_Character_BP_C")),' \
                '(NPCsToSpawnStrings=("Ptero_Character_BP_C"))' \
            '),' \
            'NPCSpawnLimits=(' \
                '(NPCClassString="Trike_Character_BP_C"),' \
                '(NPCClassString="Ptero_Character_BP_C")' \
            ')' \
        ')'

        self.test_config_dict = OrderedDict(
            {'ConfigSubtractNPCSpawnEntriesContainer': OrderedDict(
                {
                    'NPCSpawnEntriesContainerClassString': 'DinoSpawnEntriesBeach_C',
                    'NPCSpawnEntries': [
                        OrderedDict(
                            {
                                'NPCsToSpawnStrings': 'Trike_Character_BP_C'
                            }),
                        OrderedDict(
                            {
                                'NPCsToSpawnStrings': 'Ptero_Character_BP_C'
                            })
                        ],
                    'NPCSpawnLimits': [
                        OrderedDict(
                            {
                                'NPCClassString': 'Trike_Character_BP_C'
                            }),
                        OrderedDict(
                            {
                                'NPCClassString': 'Ptero_Character_BP_C'
                            })
                        ]
                    })
                })

        self.test_container_dict = OrderedDict(
            {
                'NPCSpawnEntriesContainerClassString': 'Something_C',
                'NPCSpawnEntries': [
                    OrderedDict(
                        {
                            'NPCsToSpawnStrings': 'Another_Character_BP_C'
                        })
                    ],
                'NPCSpawnLimits': [
                    OrderedDict(
                        {
                            'NPCClassString': 'Another_Character_BP_C'
                        })
                    ]
                })

        self.test_spawn_entry_dict = {
            'NPCsToSpawnStrings': 'Another_Mob_BP_C'
        }

        self.test_spawn_limit_dict = {
            'NPCClassString': 'Another_Mob_BP_C'
        }

        self.test_config = ARKConfigSubtractNPCSpawnEntriesContainer()
        self.test_config.from_string(self.test_config_string)

    def tearDown(self):
        self.test_config = None

    def test_from_string(self):
        self.assertDictEqual(
            self.test_config._config_item,
            self.test_config_dict)

    def test_to_string(self):
        self.assertEqual(
            self.test_config.to_string(self.test_config_dict),
            self.test_config_string)

    def test_add_spawn_entry(self):
        self.test_config.add_spawn_entry(self.test_spawn_entry_dict)
        container = self.test_config_dict.get('ConfigSubtractNPCSpawnEntriesContainer')
        if container.get('NPCSpawnEntriesContainerClassString') == 'DinoSpawnEntriesBeach_C':
            container.get('NPCSpawnEntries').append(self.test_spawn_entry_dict)
        self.assertDictEqual(self.test_config._config_item, self.test_config_dict)

    def test_add_spawn_limit(self):
        self.test_config.add_spawn_limit(self.test_spawn_limit_dict)
        container = self.test_config_dict.get('ConfigSubtractNPCSpawnEntriesContainer')
        if container.get('NPCSpawnEntriesContainerClassString') == 'DinoSpawnEntriesBeach_C':
            container.get('NPCSpawnLimits').append(self.test_spawn_limit_dict)
        self.assertDictEqual(self.test_config._config_item, self.test_config_dict)

    def test_del_spawn_entry(self):
        self.test_config.del_spawn_entry('GigaSpawner')
        container = self.test_config_dict.get('ConfigSubtractNPCSpawnEntriesContainer')
        if container.get('NPCSpawnEntriesContainerClassString') == 'DinoSpawnEntriesBeach_C':
            entries = container.get('NPCSpawnEntries')
            for entry in entries:
                if entry.get('AnEntryName') == 'GigaSpawner':
                    entries.remove(entry)
                    break
        self.assertDictEqual(self.test_config._config_item, self.test_config_dict)

    def test_del_spawn_limit(self):
        self.test_config.del_spawn_limit('Gigant_Character_BP_C')
        container = self.test_config_dict.get('ConfigSubtractNPCSpawnEntriesContainer')
        if container.get('NPCSpawnEntriesContainerClassString') == 'DinoSpawnEntriesBeach_C':
            spawn_limits = container.get('NPCSpawnLimits')
            for spawn_limit in spawn_limits:
                if spawn_limit.get('NPCClassString') == 'Gigant_Character_BP_C':
                    spawn_limits.remove(spawn_limit)
                    break
        self.assertDictEqual(self.test_config._config_item, self.test_config_dict)

if __name__ == '__main__':
    unittest.main()