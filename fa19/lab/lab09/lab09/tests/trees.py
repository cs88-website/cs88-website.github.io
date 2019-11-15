test = {
  'name': 'Trees',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> t = Tree(1, Tree(2))
          Error
          >>> t = Tree(1, [Tree(2)])
          >>> t.entry
          1
          >>> t.branches[0]
          Tree(2)
          >>> t.branches[0].entry
          2
          >>> t.entry = t.branches[0].entry
          >>> t
          Tree(2, [Tree(2)])
          >>> t.branches.append(Tree(4, [Tree(8)]))
          >>> len(t.branches)
          2
          >>> t.branches[0]
          Tree(2)
          >>> t.branches[1]
          Tree(4, [Tree(8)])
          """,
          'hidden': False
        }
      ],
      'scored': False,
      'type': 'wwpp'
    }
  ]
}
