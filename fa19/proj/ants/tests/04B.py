test = {
  'name': 'Problem 4B',
  'partner': 'B',
  'points': 3,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Testing Long/ShortThrower parameters
          >>> ShortThrower.food_cost
          20d533d3e06345c8bd7072212867f2d1
          # locked
          >>> LongThrower.food_cost
          20d533d3e06345c8bd7072212867f2d1
          # locked
          >>> short_t = ShortThrower()
          >>> long_t = LongThrower()
          >>> short_t.armor
          d89cf7c79d5a479b0f636734143ed5e6
          # locked
          >>> long_t.armor
          d89cf7c79d5a479b0f636734143ed5e6
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> # Test LongThrower Hit
          >>> ant = LongThrower()
          >>> in_range = Bee(2)
          >>> colony.places['tunnel_0_0'].add_insect(ant)
          >>> colony.places["tunnel_0_5"].add_insect(in_range)
          >>> ant.action(colony)
          >>> in_range.armor
          d89cf7c79d5a479b0f636734143ed5e6
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> # Testing LongThrower miss
          >>> ant = LongThrower()
          >>> out_of_range = Bee(2)
          >>> colony.places["tunnel_0_0"].add_insect(ant)
          >>> colony.places["tunnel_0_4"].add_insect(out_of_range)
          >>> ant.action(colony)
          >>> out_of_range.armor
          20d533d3e06345c8bd7072212867f2d1
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> # Testing LongThrower targets farther one
          >>> ant = LongThrower()
          >>> out_of_range = Bee(2)
          >>> in_range = Bee(2)
          >>> colony.places["tunnel_0_0"].add_insect(ant)
          >>> colony.places["tunnel_0_4"].add_insect(out_of_range)
          >>> colony.places["tunnel_0_5"].add_insect(in_range)
          >>> ant.action(colony)
          >>> out_of_range.armor
          20d533d3e06345c8bd7072212867f2d1
          # locked
          >>> in_range.armor
          d89cf7c79d5a479b0f636734143ed5e6
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> # Test ShortThrower hit
          >>> ant = ShortThrower()
          >>> in_range = Bee(2)
          >>> colony.places['tunnel_0_0'].add_insect(ant)
          >>> colony.places["tunnel_0_3"].add_insect(in_range)
          >>> ant.action(colony)
          >>> in_range.armor
          d89cf7c79d5a479b0f636734143ed5e6
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> # Testing ShortThrower miss
          >>> ant = ShortThrower()
          >>> out_of_range = Bee(2)
          >>> colony.places["tunnel_0_0"].add_insect(ant)
          >>> colony.places["tunnel_0_4"].add_insect(out_of_range)
          >>> ant.action(colony)
          >>> out_of_range.armor
          20d533d3e06345c8bd7072212867f2d1
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> # Testing ShortThrower ignores bees outside range
          >>> thrower = LongThrower()
          >>> colony.places["tunnel_0_0"].add_insect(thrower)
          >>> bee1 = Bee(1001)
          >>> bee2 = Bee(1001)
          >>> colony.places["tunnel_0_4"].add_insect(bee1)
          >>> colony.places["tunnel_0_5"].add_insect(bee2)
          >>> thrower.action(colony)
          >>> bee1.armor
          2fbc78608a47aa415fd33a20923f338d
          # locked
          >>> bee2.armor
          20e0ee99561cd5e38514075f77309e71
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> # Testing ShortThrower attacks nearest bee in range
          >>> thrower = LongThrower()
          >>> colony.places["tunnel_0_0"].add_insect(thrower)
          >>> bee1 = Bee(1001)
          >>> bee2 = Bee(1001)
          >>> colony.places["tunnel_0_5"].add_insect(bee1)
          >>> colony.places["tunnel_0_6"].add_insect(bee2)
          >>> thrower.action(colony)
          >>> bee1.armor
          20e0ee99561cd5e38514075f77309e71
          # locked
          >>> bee2.armor
          2fbc78608a47aa415fd33a20923f338d
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> # Testing if max_range is looked up in the instance
          >>> ant = ShortThrower()
          >>> ant.max_range = 10   # Buff the ant's range
          >>> colony.places["tunnel_0_0"].add_insect(ant)
          >>> bee = Bee(2)
          >>> colony.places["tunnel_0_6"].add_insect(bee)
          >>> ant.action(colony)
          >>> bee.armor
          d89cf7c79d5a479b0f636734143ed5e6
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from ants import *
      >>> hive, layout = Hive(AssaultPlan()), dry_layout
      >>> dimensions = (1, 9)
      >>> colony = AntColony(None, hive, ant_types(), layout, dimensions)
      """,
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> # Testing LongThrower Inheritance from ThrowerAnt
          >>> def new_action(self, colony):
          ...     raise NotImplementedError()
          >>> def new_throw_at(self, target):
          ...     raise NotImplementedError()
          >>> old_thrower_action = ThrowerAnt.action
          >>> old_throw_at = ThrowerAnt.throw_at
          
          >>> ThrowerAnt.action = new_action
          >>> test_long = LongThrower()
          >>> passed = 0
          >>> try:
          ...     test_long.action(colony)
          ... except NotImplementedError:
          ...     passed += 1
          >>> ThrowerAnt.action = old_thrower_action
          >>> ThrowerAnt.throw_at = new_throw_at
          >>> test_long = LongThrower()
          >>> try:
          ...     test_long.throw_at(Bee(1))
          ... except NotImplementedError:
          ...     passed += 1
          >>> ThrowerAnt.throw_at = old_throw_at
          >>> passed
          2
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Testing ShortThrower Inheritance from ThrowerAnt
          >>> def new_action(self, colony):
          ...     raise NotImplementedError()
          >>> def new_throw_at(self, target):
          ...     raise NotImplementedError()
          >>> old_thrower_action = ThrowerAnt.action
          >>> old_throw_at = ThrowerAnt.throw_at
          
          >>> ThrowerAnt.action = new_action
          >>> test_short = ShortThrower()
          >>> passed = 0
          >>> try:
          ...     test_short.action(colony)
          ... except NotImplementedError:
          ...     passed += 1
          
          >>> ThrowerAnt.action = old_thrower_action
          >>> ThrowerAnt.throw_at = new_throw_at
          >>> test_short = ShortThrower()
          >>> try:
          ...     test_short.throw_at(Bee(1))
          ... except NotImplementedError:
          ...     passed += 1
          
          >>> ThrowerAnt.throw_at = old_throw_at
          >>> passed
          2
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from ants import *
      >>> hive, layout = Hive(AssaultPlan()), dry_layout
      >>> dimensions = (1, 9)
      >>> colony = AntColony(None, hive, ant_types(), layout, dimensions)
      """,
      'teardown': r"""
      >>> ThrowerAnt.action = old_thrower_action
      >>> ThrowerAnt.throw_at = old_throw_at
      """,
      'type': 'doctest'
    }
  ]
}
