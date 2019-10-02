test = {
  'name': 'HOF',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> def even(f):
          ...     def odd(x):
          ...         if x < 0:
          ...             return f(-x)
          ...         return f(x)
          ...     return odd
          >>> steven = lambda x: x
          >>> stewart = even(steven)
          >>> stewart
          f9e2828479178acd8850630b95998adf
          # locked
          >>> stewart(61)
          ea28d37117df6c8172c0a567a2b05750
          # locked
          >>> stewart(-4)
          9ccec59144c492b582f3e1f12bb587a1
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> # Try drawing an environment diagram if you get stuck!
          >>> higher_order_lambda = lambda f: lambda x: f(x)
          >>> def cake():
          ...    print('beets')
          ...    def pie():
          ...        print('sweets')
          ...        return 'cake'
          ...    return pie
          >>> chocolate = cake()
          aff19a29968a4f8e2585fa97c19baa2e
          # locked
          >>> chocolate
          f9e2828479178acd8850630b95998adf
          # locked
          >>> chocolate()
          89ee74821c719d4e712810316c9d9bc1
          c6f1a40ecb5124fd5b97e8b8d62528e7
          # locked
          >>> more_chocolate, more_cake = chocolate(), cake
          89ee74821c719d4e712810316c9d9bc1
          # locked
          >>> more_chocolate
          c6f1a40ecb5124fd5b97e8b8d62528e7
          # locked
          >>> def snake(x, y):
          ...    if cake == more_cake:
          ...        return lambda: x + y
          ...    else:
          ...        return x + y
          >>> snake(10, 20)
          f9e2828479178acd8850630b95998adf
          # locked
          >>> snake(10, 20)()
          8252a6fc4aa289173edf0af990751a21
          # locked
          >>> cake = 'cake'
          >>> snake(10, 20)
          8252a6fc4aa289173edf0af990751a21
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
