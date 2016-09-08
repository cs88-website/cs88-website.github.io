test = {
  'name': 'Loops',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> n = 3
          >>> while n >= 0: # If this loops forever, just type Infinite Loop
          ...     n -= 1
          ...     print(n)
          00d863fa3c4c29cbaf2f51596335aa65
          1d1ffa37e6cd6ba446350252a696274f
          f18b457c7041dbb1b33aa5c5b638afc0
          b746e7f83939c69e88079cc264b2e8dc
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> n = 4
          >>> while n > 0: # If this loops forever, just type Infinite Loop
          ...     n += 1
          ...     print(n)
          c2a28ef21f8024576163a484b26188e2
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> def go(n):
          ...     if n % 2 != 0:
          ...         print(n / 2)
          ...         return
          ...     while n > 0:
          ...         print(n)
          ...         n = n // 2
          >>> go(4) # If this loops forever, just type Infinite Loop
          c25e2ea58b31844e54be2178eabf06f9
          00d863fa3c4c29cbaf2f51596335aa65
          1d1ffa37e6cd6ba446350252a696274f
          # locked
          >>> go(5) # If this loops forever, just type Infinite Loop
          eb56e9711e23d990bfb566b7b91cfa8b
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': False,
      'type': 'wwpp'
    }
  ]
}