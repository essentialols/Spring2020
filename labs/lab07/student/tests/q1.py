test = {   'hidden': False,
    'name': 'q1',
    'points': 4,
    'suites': [   {   'cases': [   {   'code': '>>> X.columns\n'
                                               "Index(['intercept', 'LSTAT'], "
                                               "dtype='object')",
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> X.shape\n(506, 2)',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> np.all(y == '
                                               "housing['MEDV'])\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': ">>> np.all(X['intercept'] == "
                                               '1)\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': ">>> np.all(X['LSTAT'] == "
                                               "housing['LSTAT'])\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
