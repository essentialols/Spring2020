test = {   'hidden': True,
    'name': 'q4a',
    'points': 10,
    'suites': [   {   'cases': [   {   'code': '>>> \n>>> len(allaqi)\n38479',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> \n'
                                               '>>> '
                                               '(set(tmpdf.columns)-set(allaqi.columns)) '
                                               "== {'County', 'State'}\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> \n'
                                               '>>> len(allaqi.index.unique()) '
                                               '== len(allaqi)\n'
                                               'False',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
