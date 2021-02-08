import unittest
from collections import OrderedDict
from confighandlers.configoverridenpcspawnentriescontainer import ARKConfigOverrideNPCSpawnEntriesContainer


class TestARKConfigOverrideNPCSpawnEntriesContainer(unittest.TestCase):
    def setUp(self):
        self.test_config_string = 'ConfigOverrideNPCSpawnEntriesContainer=(' \
	        'NPCSpawnEntriesContainerClassString="DinoSpawnEntriesBeach_C",' \
		    'NPCSpawnEntries=(' \
			    '(AnEntryName="DragonSpawner",' \
                'EntryWeight="1000.0",' \
                'NPCsToSpawnStrings=("Dragon_Character_BP_C")),' \
			    '(AnEntryName="UnicornSpawner",' \
                'EntryWeight="1000.0",' \
                'NPCsToSpawnStrings=("Equus_Character_BP_Unicorn_C"))' \
		    '),' \
		    'NPCSpawnLimits=(' \
			    '(NPCClassString="Dragon_Character_BP_C",' \
                'MaxPercentageOfDesiredNumToAllow="0.01"),' \
			    '(NPCClassString="Equus_Character_BP_Unicorn_C",' \
                'MaxPercentageOfDesiredNumToAllow="0.01")' \
		    ')' \
        ')'

        self.test_config_item = OrderedDict(
            {'ConfigOverrideNPCSpawnEntriesContainer': OrderedDict({
                'NPCSpawnEntriesContainerClassString': 'DinoSpawnEntriesBeach_C',
                'NPCSpawnEntries': [
                    OrderedDict({
                        'AnEntryName': 'DragonSpawner',
                        'EntryWeight': '1000.0',
                        'NPCsToSpawnStrings': 'Dragon_Character_BP_C'
                    }),
                    OrderedDict({
                        'AnEntryName': 'UnicornSpawner',
                        'EntryWeight': '1000.0',
                        'NPCsToSpawnStrings': 'Equus_Character_BP_Unicorn_C'
                    })
                ],
                'NPCSpawnLimits': [
                    OrderedDict({
                        'NPCClassString': 'Dragon_Character_BP_C',
                        'MaxPercentageOfDesiredNumToAllow': '0.01'
                    }),
                    OrderedDict({
                        'NPCClassString': 'Equus_Character_BP_Unicorn_C',
                        'MaxPercentageOfDesiredNumToAllow': '0.01'
                    })
                ]
            })
        })

        self.test_spawn_entry_dict = OrderedDict({
            'AnEntryName': 'AnotherTestSpawner',
            'EntryWeight': '1000.0',
            'NPCsToSpawnStrings': 'Test_Char_BP_C'
        })

        self.test_spawn_limit_dict = OrderedDict({
            'NPCClassString': 'Another_Char_BP_C',
            'MaxPercentageOfDesiredNumToAllow': '0.01'
        })

        self.test_config = ARKConfigOverrideNPCSpawnEntriesContainer()
        self.test_config.from_string(self.test_config_string)

    def tearDown(self):
        self.test_config = None

    def test_from_string(self):
        self.assertDictEqual(
            self.test_config.config_item,
            self.test_config_item)

    def test_to_string(self):
        self.assertEqual(
            self.test_config.to_string(),
            self.test_config_string)

    def test_add_spawn_entry(self):
        self.test_config.add_spawn_entry('DinoSpawnEntriesBeach_C', self.test_spawn_entry_dict)
        container = self.test_config_item.get('ConfigOverrideNPCSpawnEntriesContainer')
        if container.get('NPCSpawnEntriesContainerClassString') == 'DinoSpawnEntriesBeach_C':
            container.get('NPCSpawnEntries').append(self.test_spawn_entry_dict)
        self.assertDictEqual(self.test_config._config_item, self.test_config_item)

    def test_add_spawn_limit(self):
        self.test_config.add_spawn_limit('DinoSpawnEntriesBeach_C', self.test_spawn_limit_dict)
        container = self.test_config_item.get('ConfigOverrideNPCSpawnEntriesContainer')
        if container.get('NPCSpawnEntriesContainerClassString') == 'DinoSpawnEntriesBeach_C':
            container.get('NPCSpawnLimits').append(self.test_spawn_limit_dict)
        self.assertDictEqual(self.test_config._config_item, self.test_config_item)

    def test_del_spawn_entry(self):
        self.test_config.del_spawn_entry('DinoSpawnEntriesBeach_C', 'GigaSpawner')
        container = self.test_config_item.get('ConfigOverrideNPCSpawnEntriesContainer')
        if container.get('NPCSpawnEntriesContainerClassString') == 'DinoSpawnEntriesBeach_C':
            entries = container.get('NPCSpawnEntries')
            for entry in entries:
                if entry.get('AnEntryName') == 'GigaSpawner':
                    entries.remove(entry)
                    break
        self.assertDictEqual(self.test_config._config_item, self.test_config_item)

    def test_del_spawn_limit(self):
        self.test_config.del_spawn_limit(
            'DinoSpawnEntriesBeach_C',
            'Gigant_Character_BP_C')
        container = self.test_config_item.get('ConfigOverrideNPCSpawnEntriesContainer')
        if container.get('NPCSpawnEntriesContainerClassString') == 'DinoSpawnEntriesBeach_C':
            spawn_limits = container.get('NPCSpawnLimits')
            for spawn_limit in spawn_limits:
                if spawn_limit.get('NPCClassString') == 'Gigant_Character_BP_C':
                    spawn_limits.remove(spawn_limit)
                    break
        self.assertDictEqual(self.test_config._config_item, self.test_config_item)

if __name__ == '__main__':
    unittest.main()
