test = {
  'name': 'Problem 2',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> WordSet("one two, Two. tHree").words()
          ['one', 'three', 'two']
          >>> WordSet(["one","two","Two", ""]).words()
          ['one', 'two']
          >>> 'two' in WordSet(["one","two","Two"])
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> Dictionary('assets/lincoln.txt').words()[55]
          'government'
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from wordset import WordSet, Dictionary
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}