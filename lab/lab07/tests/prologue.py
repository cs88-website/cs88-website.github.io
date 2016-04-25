test = {
  'name': 'Prologue',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> from car import *
          >>> johns_car = Car('Tesla')
          >>> johns_car.color
          c9ca67dd53d79be5be08fb4cf450e949
          # locked
          >>> johns_car.paint('black')
          d17d724d09c380c5d7146af0eb05dbff
          # locked
          >>> johns_car.color
          ca91611230fd51dcbccf888cd7922581
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> from car import *
          >>> johns_car = Car('Tesla')
          >>> johns_truck = MonsterTruck('Monster Truck')
          >>> johns_car.size
          3aebd9fd5746c79694a7f07e208b10c9
          # locked
          >>> johns_truck.size
          4412696077ee422f2bad2d309aa87de9
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