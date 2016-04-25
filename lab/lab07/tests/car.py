test = {
  'name': 'Car',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> from car import *
          >>> johns_car = Car('Tesla')
          >>> johns_car.model
          57fb58061c92d8dfe6d885865ea2b93c
          # locked
          >>> johns_car.gas = 10
          >>> johns_car.drive()
          e55550fd2873dd488357a03338a2cb40
          # locked
          >>> johns_car.drive()
          888627c8cc08d745a7ef5ad0d8efb991
          # locked
          >>> johns_car.fill_gas()
          e279a805331af031185c260c4b3e7907
          # locked
          >>> johns_car.gas
          cf3b881608904e51c384abfbd72a7cc8
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> from car import *
          >>> johns_car = Car('Tesla')
          >>> Car.headlights
          c9aea858aa12d15d170a9fd7596d70b1
          # locked
          >>> johns_car.headlights
          c9aea858aa12d15d170a9fd7596d70b1
          # locked
          >>> Car.headlights = 3
          >>> johns_car.headlights
          9a023de211dac9bf8558350f5fa3bdca
          # locked
          >>> johns_car.headlights = 2
          >>> Car.headlights
          9a023de211dac9bf8558350f5fa3bdca
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> from car import *
          >>> johns_car = Car('Tesla')
          >>> johns_car.wheels = 2
          >>> johns_car.wheels
          c9aea858aa12d15d170a9fd7596d70b1
          # locked
          >>> Car.num_wheels
          f2991d685f624ad59b79213e20800653
          # locked
          >>> johns_car.drive()
          888627c8cc08d745a7ef5ad0d8efb991
          # locked
          >>> Car.drive()
          795bceccbca635277a3bbfa64bc9dba0
          # locked
          >>> Car.drive(johns_car)
          888627c8cc08d745a7ef5ad0d8efb991
          # locked
          >>> MonsterTruck.drive(johns_car)
          795bceccbca635277a3bbfa64bc9dba0
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
          beba7598767b3ddfeb4b0163408184fa
          773589c2840a39c3a7ddb63a4a5c41fa
          # locked
          >>> Car.drive(sumukhs_car)
          773589c2840a39c3a7ddb63a4a5c41fa
          # locked
          >>> MonsterTruck.drive(sumukhs_car)
          beba7598767b3ddfeb4b0163408184fa
          773589c2840a39c3a7ddb63a4a5c41fa
          # locked
          >>> Car.rev(sumukhs_car)
          795bceccbca635277a3bbfa64bc9dba0
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