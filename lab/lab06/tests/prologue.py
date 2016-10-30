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
          058a4899e0e4f451de8b35121de08b60
          # locked
          >>> johns_car.paint('black')
          5f602432a4da64609c8d5c9fe2262465
          # locked
          >>> johns_car.color
          e74918d4310bb6cbc896676f20dc20de
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
          77680819e28d50de159e07d024a1683f
          # locked
          >>> johns_truck.size
          07bd1cf0e022b8f011a9680a683d13e2
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