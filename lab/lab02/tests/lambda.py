test = {
  'name': 'Lambda the Free',
  'points': 0,
  'suites': [
    {
      'type': 'wwpp',
      'cases': [
        {
          'code': """
          >>> lambda x: x # Can we access this function?
          Function
          >>> a = lambda x: x
          >>> a(5) # x is the parameter for the lambda function
          5
          >>> b = lambda: 3
          >>> b()
          3
          >>> c = lambda x: lambda: print('123')
          >>> c(88)
          Function
          >>> c(88)()
          123
          >>> d = lambda f: f(4) # They can have functions as arguments as well.
          >>> def square(x):
          ...     return x * x
          >>> d(square)
          16
          """
        },
        {
          'code': """
          >>> t = lambda f: lambda x: f(f(f(x)))
          >>> s = lambda x: x + 1
          >>> t(s)(0)
          3
          >>> bar = lambda y: lambda x: pow(x, y)
          >>> bar()(15)
          Error
          >>> foo = lambda: 32
          >>> foobar = lambda x, y: x // y
          >>> a = lambda x: foobar(foo(), bar(4)(x))
          >>> a(2)
          2
          >>> b = lambda x, y: print('summer') # When is the body of this function run?
          Nothing
          >>> c = b(4, 'dog')
          summer
          >>> print(c)
          None
          """
        },
      ]
    }
  ]
}
