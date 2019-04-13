test = {
  'name': 'Does it work?',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'answer': 'b1441d8506f54e95da548bbd3b2214a2',
          'choices': [
            'No problem, this is a beautiful iterator!',
            'Uh oh, this is missing __next__.',
            'This "iterator" doesn\'t even define __iter__.'
          ],
          'hidden': False,
          'locked': True,
          'question': r"""
          Does IteratorA work?
          
          class IteratorA:
             def __init__(self):
                 self.start = 10
          
             def __next__(self):
                 if self.start > 100:
                     raise StopIteration
                 self.start += 20
                 return self.start
          
             def __iter__(self):
                 return self
          """
        },
        {
          'answer': '7b6d9694c7f303c3f0a08df9f9cc0c9d',
          'choices': [
            'No problem, this is a beautiful iterator!',
            'Uh oh, this is missing __next__.',
            'This "iterator" doesn\'t even define __iter__.'
          ],
          'hidden': False,
          'locked': True,
          'question': r"""
          Does IteratorB work?
          
          class IteratorB:
              def __init__(self):
                  self.start = 5
          
              def __iter__(self):
                  return self
          """
        },
        {
          'answer': 'c4dfebecd5522ed75fb7cc481b2568a0',
          'choices': [
            'No problem, this is a beautiful iterator!',
            'Uh oh, this is missing __next__.',
            'This "iterator" doesn\'t even define __iter__.'
          ],
          'hidden': False,
          'locked': True,
          'question': r"""
          Does IteratorC work?
          
          class IteratorC:
              def __init__(self):
                  self.start = 5
          
              def __next__(self):
                  if self.start == 10:
                      raise StopIteration
                  self.start += 1
                  return self.start
          """
        },
        {
          'answer': 'b1441d8506f54e95da548bbd3b2214a2',
          'choices': [
            'No problem, this is a beautiful iterator!',
            'Uh oh, this is missing __next__.',
            'This "iterator" doesn\'t even define __iter__.'
          ],
          'hidden': False,
          'locked': True,
          'question': r"""
          Does IteratorD work?
          
          class IteratorD:
              def __init__(self):
                  self.start = 1
          
              def __next__(self):
                  self.start += 1
                  return self.start
          
              def __iter__(self):
                  return self
          """
        }
      ],
      'scored': False,
      'type': 'concept'
    }
  ]
}