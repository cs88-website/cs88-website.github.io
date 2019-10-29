test = {
  'name': 'Case 3',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> x = [5, 'hello', [1, 1]]
          >>> y = x[:]
          >>> y[0] = 10
          >>> y
          f0692125b51fc286b2dd24e2e007803c
          # locked
          >>> x
          e370c21adc7649f1bce8efd5fbbb078a
          # locked
          >>> z = x[:]
          >>> z[2][1] = 5
          >>> z
          86c3f001cfbc9c285798e876c9ad105b
          # locked
          >>> x
          86c3f001cfbc9c285798e876c9ad105b
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
