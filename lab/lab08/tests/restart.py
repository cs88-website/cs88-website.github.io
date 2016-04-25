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
          f688246bcd159bb0cf67948057d5fb79
          # locked
          >>> [num for num in iterator]
          573f7f1134c5dde12d8bbcb699fd59f9
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