test = {
  'name': 'Car',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> from car import *
          >>> srinaths_car = Car('Tesla', 'Model S')
          >>> srinaths_car.model
          066daa99c4c14fba33ca7fea6de5139e
          # locked
          >>> srinaths_car.gas = 10
          >>> srinaths_car.drive()
          6782dfbb8a7616b3f504afa7bdbc4efe
          # locked
          >>> srinaths_car.drive()
          85ac99d9ea4aac334a8bfe842d10c09d
          # locked
          >>> srinaths_car.fill_gas()
          7b0c88ff69d31a8e50f681edcc9d6ef5
          # locked
          >>> srinaths_car.gas
          2b5c8adf725274c931c4272b26ac97ea
          # locked
          >>> Car.gas
          e0c9124d3360b0721b517ec33d41b017
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> from car import *
          >>> srinaths_car = Car('Tesla', 'Model S')
          >>> srinaths_car.wheels = 2
          >>> srinaths_car.wheels
          9338923f09aac77121029c604f7ce4f3
          # locked
          >>> Car.num_wheels
          612ff2a71cad53bc4c7f85fac678a06d
          # locked
          >>> srinaths_car.drive() # Type Error if an error occurs and Nothing if nothing is displayed
          85ac99d9ea4aac334a8bfe842d10c09d
          # locked
          >>> Car.drive() # Type Error if an error occurs and Nothing if nothing is displayed
          8a2fd4e4c3c6dcce2dc631af62ee217a
          # locked
          >>> Car.drive(srinaths_car) # Type Error if an error occurs and Nothing if nothing is displayed
          85ac99d9ea4aac334a8bfe842d10c09d
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
