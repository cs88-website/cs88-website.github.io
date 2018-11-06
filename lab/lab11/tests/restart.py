test = {
  'name': 'Restart',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> class IteratorA:
          ...    def __init__(self):
          ...        self.start = 10
          ...    def __next__(self):
          ...        if self.start > 100:
          ...            raise StopIteration
          ...        self.start += 20
          ...        return self.start
          ...    def __iter__(self):
          ...        return self
          >>> iterator = IteratorA()
          >>> [num for num in iterator]
          d9e9ce9e113c6e01c8489077f0a07f46
          # locked
          >>> [num for num in iterator]
          1f73c5ccb26eee699414362be850992d
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