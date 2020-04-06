test = {   'hidden': False,
    'name': 'q5e',
    'points': 5,
    'suites': [   {   'cases': [   {   'code': '>>> \n'
                                               '>>> '
                                               'len(bootstrap_data_means(election_sub))\n'
                                               '19',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> \n'
                                               '>>> all(election_agg.index == '
                                               'bootstrap_data_means(election_sub).index)\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> \n'
                                               ">>> 'mean' in "
                                               'bootstrap_data_means(election_sub).columns\n'
                                               'False',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> \n'
                                               '>>> '
                                               'bootstrap_election_100_agg.shape\n'
                                               '(19, 100)',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
