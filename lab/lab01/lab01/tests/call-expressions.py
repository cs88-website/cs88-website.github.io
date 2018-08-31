test = {
  'name': 'call-expressions',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> from operator import mul, add
          >>> mul(3, 4)
          d7069594fd949c78b4021fc7911322a4
          # locked
          >>> mul(3, add(4, 1))
          438f344a520081fe8e2d0da944a5240b
          # locked
          >>> pow(2, 3)
          44b009a8ae29e806844d66237881d263
          # locked
          >>> pow(pow(2, 3), abs(-2))
          b87d7bccbca9251a446d3bd43ad00973
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> from math import sqrt
          >>> sqrt(144)
          7925eab2931ff04d3fd1eca7688a537b
          # locked
          >>> pi
          d7b5fd49f83e4ee318af207fc969c9f4
          # locked
          >>> from math import pi
          >>> pi
          1fdff3e2f9fb8ede0322356723aae485
          # locked
          >>> print(add(9, 1))
          32606b4d8bc69544a1579aca287813dc
          # locked
          >>> print(print(2))
          6d6f378f0affa7f84aa38e519e353617
          140b47bd322af58a8e4cce7e526bedeb
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