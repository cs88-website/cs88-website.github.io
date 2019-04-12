test = {
  'name': 'Problem 2',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> WordSet("one two, Two. tHree").words()
          8019ac13d675f2965a069f8b9c3ce2a4
          # locked
          >>> WordSet(["one","two","Two", ""]).words()
          504a617a51598da12ae1647f26c2088f
          # locked
          >>> 'two' in WordSet(["one","two","Two"])
          59726c01afda154abf6bc7c1aa901742
          # locked
          """,
          'hidden': False,
          'locked': True
        },
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