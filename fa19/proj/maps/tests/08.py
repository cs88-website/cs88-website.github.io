test = {
  'name': 'Problem 8',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'answer': 'a1b936b987dd1d8e04c4ca1970f64dea',
          'choices': [
            'a list of restaurants reviewed by the user',
            'a list of all possible restaurants',
            'a list of ratings for restaurants reviewed by the user'
          ],
          'hidden': False,
          'locked': True,
          'question': 'In best_predictor, what does the variable reviewed represent?'
        },
        {
          'answer': '6475a841cb2f9e38aa3e8e45b29e5994',
          'choices': [
            'a predictor function, and its r_squared value',
            'a predictor function',
            'an r_squared value',
            'a restaurant'
          ],
          'hidden': False,
          'locked': True,
          'question': r"""
          Given a user, a list of restaurants, and a feature function, what
          does find_predictor from Problem 7 return?
          """
        },
        {
          'answer': '8e8fe1252dbcb2c041434d22d0655313',
          'choices': [
            'the predictor with the highest r_squared',
            'the predictor with the lowest r_squared',
            'the first predictor in the list',
            'an arbitrary predictor'
          ],
          'hidden': False,
          'locked': True,
          'question': r"""
          After getting a list of [predictor, r_squared] pairs,
          which predictor should we select?
          """
        }
      ],
      'scored': False,
      'type': 'concept'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> user = make_user('Cheapskate', [
          ...     make_review('A', 2),
          ...     make_review('B', 5),
          ...     make_review('C', 2),
          ...     make_review('D', 5),
          ... ])
          >>> cluster = [
          ...     make_restaurant('A', [5, 2], [], 4, [
          ...         make_review('A', 5)
          ...     ]),
          ...     make_restaurant('B', [3, 2], [], 2, [
          ...         make_review('B', 5)
          ...     ]),
          ...     make_restaurant('C', [-2, 6], [], 4, [
          ...         make_review('C', 4)
          ...     ]),
          ...     make_restaurant('D', [4, 2], [], 2, [
          ...         make_review('D', 3),
          ...         make_review('D', 4)
          ...     ]),
          ... ]
          >>> fns = [restaurant_price, restaurant_mean_rating]
          >>> pred = best_predictor(user, cluster, fns)
          >>> [round(pred(r), 5) for r in cluster] # should be a list of decimals
          [2.0, 5.0, 2.0, 5.0]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> user = make_user('Cheapskate', [
          ...     make_review('A', 2),
          ...     make_review('B', 5),
          ...     make_review('C', 2),
          ...     make_review('D', 5),
          ... ])
          >>> cluster = [
          ...     make_restaurant('A', [5, 2], [], 4, [
          ...         make_review('A', 5)
          ...     ]),
          ...     make_restaurant('B', [3, 2], [], 2, [
          ...         make_review('B', 5)
          ...     ]),
          ...     make_restaurant('C', [-2, 6], [], 4, [
          ...         make_review('C', 4)
          ...     ]),
          ... ]
          >>> fns = [restaurant_price, restaurant_mean_rating]
          >>> pred = best_predictor(user, cluster, fns)
          >>> [round(pred(r), 5) for r in cluster]
          [2.0, 5.0, 2.0]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> user = make_user('Cheapskate', [
          ...     make_review('A', 2),
          ...     make_review('B', 5),
          ...     make_review('C', 2),
          ...     make_review('D', 5),
          ... ])
          >>> cluster = [
          ...     make_restaurant('A', [5, 2], [], 4, [
          ...         make_review('A', 5)
          ...     ]),
          ...     make_restaurant('B', [3, 2], [], 2, [
          ...         make_review('B', 5)
          ...     ]),
          ...     make_restaurant('C', [-2, 6], [], 4, [
          ...         make_review('C', 4)
          ...     ]),
          ... ]
          >>> fns = [restaurant_mean_rating, restaurant_price]
          >>> pred = best_predictor(user, cluster, fns)
          >>> [round(pred(r), 5) for r in cluster] # Make sure you're iterating through feature_fns!
          [2.0, 5.0, 2.0]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> user = make_user('Cheapskate', [
          ...     make_review('A', 2),
          ...     make_review('B', 5),
          ...     make_review('C', 2),
          ...     make_review('D', 5),
          ... ])
          >>> cluster = [
          ...     make_restaurant('A', [5, 2], [], 4, [
          ...         make_review('A', 5)
          ...     ]),
          ...     make_restaurant('B', [3, 2], [], 2, [
          ...         make_review('B', 5)
          ...     ]),
          ...     make_restaurant('C', [-2, 6], [], 4, [
          ...         make_review('C', 4)
          ...     ]),
          ...     make_restaurant('E', [1, 2], [], 4, [
          ...         make_review('E', 4)
          ...     ]),
          ... ]
          >>> fns = [restaurant_mean_rating, restaurant_price]
          >>> pred = best_predictor(user, cluster, fns) # Make sure you're only using user-reviewed restaurants!
          >>> [round(pred(r), 5) for r in cluster]
          [2.0, 5.0, 2.0, 2.0]
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> import tests.test_functions as test
      >>> from recommend import *
      """,
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> user = make_user('Cheapskate', [
          ...     make_review('A', 2),
          ...     make_review('B', 5),
          ...     make_review('C', 2),
          ...     make_review('D', 5),
          ... ])
          >>> cluster = [
          ...     make_restaurant('A', [5, 2], [], 4, [
          ...         make_review('A', 5)
          ...     ]),
          ...     make_restaurant('B', [3, 2], [], 2, [
          ...         make_review('B', 5)
          ...     ]),
          ...     make_restaurant('C', [-2, 6], [], 4, [
          ...         make_review('C', 4)
          ...     ]),
          ...     make_restaurant('D', [4, 2], [], 2, [
          ...         make_review('D', 3),
          ...         make_review('D', 4)
          ...     ]),
          ... ]
          >>> fns = [restaurant_price, restaurant_mean_rating]
          >>> pred = best_predictor(user, cluster, fns)
          >>> # Hint: Price is a perfect predictor of this user's ratings,
          >>> #       so the predicted ratings should equal the user's ratings
          >>> [round(pred(r), 5) for r in cluster] # should be a list of decimals
          [2.0, 5.0, 2.0, 5.0]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> user = make_user('Cheapskate', [
          ...     make_review('A', 2),
          ...     make_review('B', 5),
          ...     make_review('C', 2),
          ...     make_review('D', 5),
          ... ])
          >>> cluster = [
          ...     make_restaurant('A', [5, 2], [], 4, [
          ...         make_review('A', 5)
          ...     ]),
          ...     make_restaurant('B', [3, 2], [], 2, [
          ...         make_review('B', 5)
          ...     ]),
          ...     make_restaurant('C', [-2, 6], [], 4, [
          ...         make_review('C', 4)
          ...     ]),
          ... ]
          >>> fns = [restaurant_price, restaurant_mean_rating]
          >>> pred = best_predictor(user, cluster, fns)
          >>> [round(pred(r), 5) for r in cluster]
          [2.0, 5.0, 2.0]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> user = make_user('Cheapskate', [
          ...     make_review('A', 2),
          ...     make_review('B', 5),
          ...     make_review('C', 2),
          ...     make_review('D', 5),
          ... ])
          >>> cluster = [
          ...     make_restaurant('A', [5, 2], [], 4, [
          ...         make_review('A', 5)
          ...     ]),
          ...     make_restaurant('B', [3, 2], [], 2, [
          ...         make_review('B', 5)
          ...     ]),
          ...     make_restaurant('C', [-2, 6], [], 4, [
          ...         make_review('C', 4)
          ...     ]),
          ... ]
          >>> fns = [restaurant_mean_rating, restaurant_price]
          >>> pred = best_predictor(user, cluster, fns)
          >>> [round(pred(r), 5) for r in cluster] # Make sure you're iterating through feature_fns!
          [2.0, 5.0, 2.0]
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> user = make_user('Cheapskate', [
          ...     make_review('A', 2),
          ...     make_review('B', 5),
          ...     make_review('C', 2),
          ...     make_review('D', 5),
          ... ])
          >>> cluster = [
          ...     make_restaurant('A', [5, 2], [], 4, [
          ...         make_review('A', 5)
          ...     ]),
          ...     make_restaurant('B', [3, 2], [], 2, [
          ...         make_review('B', 5)
          ...     ]),
          ...     make_restaurant('C', [-2, 6], [], 4, [
          ...         make_review('C', 4)
          ...     ]),
          ...     make_restaurant('E', [1, 2], [], 4, [
          ...         make_review('E', 4)
          ...     ]),
          ... ]
          >>> fns = [restaurant_mean_rating, restaurant_price]
          >>> pred = best_predictor(user, cluster, fns) # Make sure you're only using user-reviewed restaurants!
          >>> [round(pred(r), 5) for r in cluster]
          [2.0, 5.0, 2.0, 2.0]
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> import tests.test_functions as test
      >>> import recommend
      >>> test.swap_implementations(recommend)
      >>> from recommend import *
      """,
      'teardown': r"""
      >>> test.restore_implementations(recommend)
      """,
      'type': 'doctest'
    }
  ]
}
