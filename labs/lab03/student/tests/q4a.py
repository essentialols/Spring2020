test = {   'hidden': False,
    'name': 'q4a',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': '>>> import matplotlib ;\n'
                                               '>>> '
                                               'np.alltrue(np.array([l.get_text() '
                                               'for l in '
                                               'ax_4a.xaxis.get_ticklabels()]) '
                                               '== days)\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> bars = [rect.get_height() '
                                               'for rect in '
                                               'ax_4a.get_children() \n'
                                               '...         if '
                                               'isinstance(rect, '
                                               'matplotlib.patches.Rectangle) '
                                               'and rect.get_x() != 0.0\n'
                                               '...        ];\n'
                                               '>>> '
                                               'np.allclose(np.array(bars)[-3:], '
                                               '[1, 1, 2])\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
