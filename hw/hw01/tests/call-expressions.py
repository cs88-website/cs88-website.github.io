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
          0c5bacbb5aa8efa98a98d240383bf633
          # locked
          >>> mul(3, add(4, 1))
          95957b6860bf3a30b229da4a41866ade
          # locked
          >>> pow(2, 3)
          671ed54989b8b2d016a764f4eb59e6f8
          # locked
          >>> pow(pow(2, 3), abs(-2))
          636a955b889c15b5068e35f1317fd581
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> from math import sqrt
          >>> sqrt(144)
          0c5bacbb5aa8efa98a98d240383bf633
          # locked
          >>> pi
          dfda46f58105eb6e5be6c5c5ab7b6eb1
          # locked
          >>> from math import pi
          >>> pi # round to 2 decimal places
          064dd9757f5e3e880843a6f8acd7fb32
          # locked
          >>> from operator import add
          >>> print(add(9, 1))
          56057c93219ebaa36c14e3a5c2c6adc1
          # locked
          >>> print(print(2))
          0e848c28f96df07c693ef539595d4380
          84223991e4180c1b5055fe16fc7125a3
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