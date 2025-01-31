import cheapestVehicle, unittest

class testCheapestVehicle(unittest.TestCase):
    def testCalcVehicleCost(self):
        # van
        self.assertEqual(cheapestVehicle.calcVehicleCost(0, 37, 10, 1, 1), 37) 
        self.assertEqual(cheapestVehicle.calcVehicleCost(100, 37, 10, 1, 1), 47)
        self.assertEqual(cheapestVehicle.calcVehicleCost(100.44, 37, 10, 1, 1), 47.04)

        # lorry 
        self.assertEqual(cheapestVehicle.calcVehicleCost(0, 47, 53, 1, 0.354006), 47)
        self.assertEqual(cheapestVehicle.calcVehicleCost(100, 47, 53, 1, 0.354006), 52.33)
        self.assertEqual(cheapestVehicle.calcVehicleCost(100.44, 47, 53, 1, 0.354006), 52.35)

        # barge
        self.assertEqual(cheapestVehicle.calcVehicleCost(0, 47, 78, 1, 0.4074), 47)
        self.assertEqual(cheapestVehicle.calcVehicleCost(100, 47, 78, 1, 0.4074), 50.15)
        self.assertEqual(cheapestVehicle.calcVehicleCost(100.44, 47, 78, 1, 0.4074), 50.16)

    def testGetCheapestVehicle(self):  
        vehicles = [ 
                {'name': 'Van', 'total_cost': 190},
                {'name': 'Lorry', 'total_cost': 210},
                {'name': 'Barge', 'total_cost': 200}
            ]
        self.assertEqual(cheapestVehicle.getCheapestVehicle(vehicles), {'name': 'Van', 'total_cost': 190})

        vehicles = [ 
                {'name': 'Van', 'total_cost': 250},
                {'name': 'Lorry', 'total_cost': 200},
                {'name': 'Barge', 'total_cost': 210}
            ]
        self.assertEqual(cheapestVehicle.getCheapestVehicle(vehicles), {'name': 'Lorry', 'total_cost': 200})
        
        vehicles = [ 
                {'name': 'Van', 'total_cost': 250},
                {'name': 'Lorry', 'total_cost': 210},
                {'name': 'Barge', 'total_cost': 200}
            ]
        self.assertEqual(cheapestVehicle.getCheapestVehicle(vehicles), {'name': 'Barge', 'total_cost': 200})