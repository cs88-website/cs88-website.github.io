test = {
  'name': 'Problem 1',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> s = SecretWord('whodoneit')
          >>> len(s)
          a8ca43461a710f7104a2e2ebfddef02e
          # locked
          >>> s.match('o')
          dd7b8b065ca91b083ea661ac42418c94
          # locked
          >>> s.match('x')
          8ed1f644a341f4041c073b56ff1d727a
          # locked
          >>> s
          712f22c791b39f8b5413daea52ed0f97
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> s = SecretWord('whodoneit')
          >>> len(s)
          9
          >>> s.match('o')
          [2, 4]
          >>> s.match('x')
          []
          >>> s
          <secret word>
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from secret import *
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}