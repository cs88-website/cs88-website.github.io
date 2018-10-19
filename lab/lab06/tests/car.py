test = {
  'name': 'Car',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> from car import *
          >>> raquels_car = Car('Tesla')
          >>> raquels_car.model
          4637c36baa2a7b15b42041c4f4eb1f0e
          # locked
          >>> raquels_car.gas = 10
          >>> raquels_car.drive()
          f7eb445770683ea938e01c464ee0ffa1
          # locked
          >>> raquels_car.drive()
          df7c85b28b8be1d389a74508ee81e8cd
          # locked
          >>> raquels_car.fill_gas()
          c0e5eff108e787b15de63424867085d6
          # locked
          >>> raquels_car.gas
          1987bce9c137ee1be913e29126e18d3c
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> from car import *
          >>> raquels_car = Car('Tesla')
          >>> Car.headlights
          d05bc830613dfa69ef96df4f94a8da70
          # locked
          >>> raquels_car.headlights
          d05bc830613dfa69ef96df4f94a8da70
          # locked
          >>> Car.headlights = 3
          >>> raquels_car.headlights
          214f1f0cf62380259278c29f0dd9185d
          # locked
          >>> raquels_car.headlights = 2
          >>> Car.headlights
          214f1f0cf62380259278c29f0dd9185d
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> from car import *
          >>> raquels_car = Car('Tesla')
          >>> raquels_car.wheels = 2
          >>> raquels_car.wheels
          d05bc830613dfa69ef96df4f94a8da70
          # locked
          >>> Car.num_wheels
          41cc26e29cc2a9e0b6fb880e349243bb
          # locked
          >>> raquels_car.drive()
          df7c85b28b8be1d389a74508ee81e8cd
          # locked
          >>> Car.drive()
          34db8258c24aff02f4e0aeaa32af407b
          # locked
          >>> Car.drive(raquels_car)
          df7c85b28b8be1d389a74508ee81e8cd
          # locked
          >>> MonsterTruck.drive(raquels_car)
          34db8258c24aff02f4e0aeaa32af407b
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> from car import *
          >>> sumukhs_car = MonsterTruck('Batmobile')
          >>> sumukhs_car.drive()
          238e48b17a8085331a1d671045b7a572
          3a03e21a02df84fa20699bc73c3c942b
          # locked
          >>> Car.drive(sumukhs_car)
          3a03e21a02df84fa20699bc73c3c942b
          # locked
          >>> MonsterTruck.drive(sumukhs_car)
          238e48b17a8085331a1d671045b7a572
          3a03e21a02df84fa20699bc73c3c942b
          # locked
          >>> Car.rev(sumukhs_car)
          34db8258c24aff02f4e0aeaa32af407b
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