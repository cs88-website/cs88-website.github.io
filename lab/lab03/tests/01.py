test = {
  'name': 'Question 1.2',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> from lab03 import *
          >>> fruitCart = [("apple", 0.5, 3), ("banana", 0.25, 4)]
          >>> taxedFruit = tax(fruitCart, 10)
          >>> cartSum(taxedFruit)
          7c0b2b63c62dfc2517d61470182f2458
          # locked
          >>> calCart = [("oski", 1000, 1), ("go", 1.25, 2), ("bears", 3.5, 2)]
          >>> taxedCal = tax(calCart, 100)
          >>> cartSum(taxedCal)
          47c3200c2b2807bbddde9932dd0ce818
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