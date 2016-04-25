test = {
  'name': 'Generators',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> def generator():
          ...     print("Starting here")
          ...     i = 0
          ...     while i < 6:
          ...         print("Before yield")
          ...         yield i
          ...         print("After yield")
          ...         i += 1
          >>> g = generator() # what type of object is g?
          >>> g == iter(g) # True or False?
          0528ddea472f19174e0c4eb75b4de3de
          # locked
          >>> next(g) # equivalent of g.__next__()
          ecc5bf542f329add48018a0dd8bacb19
          2f1499ea9e8a55e56fd7c2f0baa0b695
          7c2ddff07764c87227f4781f812caaa6
          # locked
          >>> next(g)
          74028ad3c44f9dca0987ebc99355fafc
          2f1499ea9e8a55e56fd7c2f0baa0b695
          802285b020b27240a3824a7e42f8cc8c
          # locked
          >>> next(g)
          74028ad3c44f9dca0987ebc99355fafc
          2f1499ea9e8a55e56fd7c2f0baa0b695
          9338923f09aac77121029c604f7ce4f3
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