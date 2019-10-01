test = {
  'name': 'Lambda the Free',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'answer': '3b7eba9462463de5f983d5101828fe8e',
          'choices': [
            'A lambda expression does not automatically bind the function object that it returns to any name.',
            'A lambda expression cannot have more than two parameters.',
            'A lambda expression cannot return another function.',
            'A def statement can only have one line in its body.'
          ],
          'hidden': False,
          'locked': True,
          'question': r"""
          Which of the following statements describes a difference between a def statement
          and a lambda expression?
          """
        },
        {
          'answer': 'b76782bcca4e5d30223261e64bb1b08c',
          'choices': [
            'one',
            'two',
            'three',
            'Not enough information'
          ],
          'hidden': False,
          'locked': True,
          'question': r"""
          How many parameters does the following lambda expression have?
          lambda a, b: c + d
          """
        },
        {
          'answer': 'fd19d8fb594c3dd5615f806e93d3b94a',
          'choices': [
            'When the function returned by the lambda expression is called.',
            'When you assign the lambda expression to a name.',
            'When the lambda expression is evaluated.',
            'When you pass the lambda expression into another function.'
          ],
          'hidden': False,
          'locked': True,
          'question': 'When is the return expression of a lambda expression executed?'
        }
      ],
      'scored': False,
      'type': 'concept'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> lambda x: x  # A lambda expression with one parameter x
          f9e2828479178acd8850630b95998adf
          # locked
          >>> a = lambda x: x  # Assigning a lambda function to the name a
          >>> a(5)
          7e1fd084fd9f521ed63ed94b33b2ebc9
          # locked
          >>> (lambda: 3)()  # Using a lambda expression as an operator in a call exp.
          145b04e603caaff9f94bd4fed17494c0
          # locked
          >>> b = lambda x: lambda: x  # Lambdas can return other lambdas!
          >>> c = b(88)
          >>> c
          f9e2828479178acd8850630b95998adf
          # locked
          >>> c()
          540fe450f85ae4ade11c5de9e3653515
          # locked
          >>> d = lambda f: f(4)  # They can have functions as arguments as well
          >>> def square(x):
          ...     return x * x
          >>> d(square)
          ced8e428597bcff14365fe582d9f8c0e
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> x = None # remember to review the rules of WWPD given above!
          >>> x
          >>> lambda x: x
          f9e2828479178acd8850630b95998adf
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> #
          >>> # Pay attention to the scope of variables
          >>> z = 3
          >>> e = lambda x: lambda y: lambda: x + y + z
          >>> e(0)(1)()
          9ccec59144c492b582f3e1f12bb587a1
          # locked
          >>> f = lambda z: x + z
          >>> f(3)
          1f163ffe97bf25f651f5be25cb808b6e
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> # Try drawing an environment diagram if you get stuck!
          >>> higher_order_lambda = lambda f: lambda x: f(x)
          >>> g = lambda x: x * x
          >>> higher_order_lambda(2)(g) # Which argument belongs to which function call?
          1f163ffe97bf25f651f5be25cb808b6e
          # locked
          >>> higher_order_lambda(g)(2)
          9ccec59144c492b582f3e1f12bb587a1
          # locked
          >>> call_thrice = lambda f: lambda x: f(f(f(x)))
          >>> call_thrice(lambda y: y + 1)(0)
          145b04e603caaff9f94bd4fed17494c0
          # locked
          >>> print_lambda = lambda z: print(z)
          >>> print_lambda
          f9e2828479178acd8850630b95998adf
          # locked
          >>> one_thousand = print_lambda(1000)
          3a9e7481f335ce9e68c6b76a123864d2
          # locked
          >>> one_thousand
          c528cd1c6f18f16a76fa8063144e63c5
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
