OK_FORMAT = True

test = {   'name': 'q4_3',
    'points': None,
    'suites': [   {   'cases': [   {'code': '>>> # It looks like your maximums array is empty!\n>>> len(maximums) != 0\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> len(maximums) == 5000\nTrue', 'hidden': False, 'locked': False},
                                   {   'code': ">>> # The biggest simulated maximum can't be bigger than the actual maximum!\n>>> max(maximums) <= max(earthquakes.column('mag'))\nTrue",
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
