test = {
  'name': 'Problem 3',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'answer': '9c9ae59b808cf24bbbc76a9d6724fd26',
          'choices': [
            'number; e.g. 1',
            "restaurant; e.g. make_restaurant('A', [1, 1], ['Food'], 1, [])",
            'pair; e.g. [1, 1]',
            "string of a pair; e.g. '[1, 1]'"
          ],
          'hidden': False,
          'locked': True,
          'question': r"""
          Which of the following types of values can be passed as
          an argument to distance?
          """
        },
        {
          'answer': '65e740a5296d2f5365f3d586af64700c',
          'choices': [
            'lambda x, y: pow(-x, y)',
            'lambda x, y: abs(x - y)',
            'lambda x: abs(x[0] - x[1])',
            'sum'
          ],
          'hidden': False,
          'locked': True,
          'question': r"""
          Consider the list l = [[4, 1], [-3, 2], [5, 0]]. Which of
          the choices below for fn would make min(l, key=fn) evaluate
          to [4, 1]?
          """
        }
      ],
      'scored': False,
      'type': 'concept'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> distance([0, 0], [3, 4]) # should be a decimal
          a15951e5057c787b8772cbe987c7df6e
          # locked
          >>> distance([6, 1], [6, 1]) # should be a decimal
          537d72d7c992ba8b57a4f72133f5e8b7
          # locked
          >>> distance([-2, 7], [-3.5, 9]) # should be a decimal
          80097a673c0352c4b5464ee5ad6a788e
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> find_closest([6, 1],
          ...              [[1, 5], [3, 3]])
          cf0ab5886c61bf8feb964e28b7b3c336
          # locked
          >>> find_closest([1, 6],
          ...              [[1, 5], [3, 3]])
          a68ad37530ca58e37d42c1e6cf6b25ef
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> find_closest([0, 0],
          ...              [[-2, 0], [2, 0]])
          4784c326ffb5331e44034a0ebf86eed3
          # locked
          >>> find_closest([0, 0],
          ...              [[1000, 1000]])
          311bcea6935d7ea7cc662c793b484621
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> # be sure to use the distance function!
          >>> find_closest([0, 0],
          ...              [[2, 2], [0, 3]])
          44cc6ae4a474294a05cdfc1e57addc1a
          # locked
          >>> find_closest([0, 0],
          ...              [[5, 5], [2, 7]])
          cb9b6e0e5c0db9ff7593e1966ebe623c
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': True,
      'setup': r"""
      >>> import tests.test_functions as test
      >>> from recommend import *
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
