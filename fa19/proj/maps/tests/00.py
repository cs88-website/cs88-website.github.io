test = {
  'name': 'Problem 0',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> square = lambda x: x * x
          >>> is_odd = lambda x: x % 2 == 1
          >>> map_and_filter([1, 2, 3, 4, 5], square, is_odd)
          d7483451bbef144118cb63ea9b97acfb
          # locked
          >>> map_and_filter(['hi', 'hello', 'hey', 'world'],
          ...                lambda x: x[4], lambda x: len(x) > 4)
          6e8cfabbdca3d8d2e57972ea65156e9b
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> key_of_min_value({1: 6, 2: 5, 3: 4})
          bf781112d85f9ba641fb92c424afcfc4
          # locked
          >>> key_of_min_value({'a': 6, 'b': 5, 'c': 4})
          0b66e07674e35e207b74b4ba8f313500
          # locked
          >>> key_of_min_value({'hello': 'world', 'hi': 'there'})
          e17fff0bfc4df2293b4360a3025c5c7b
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> enumerate([6, 'one', 'a'], 3)[1]
          daeb2f77f64814cde803b66f350d3079
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from utils import *
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
