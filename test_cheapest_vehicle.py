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
        listOfVehicles = [
            {'name': 'Van', 'cost': 100},
            {'name': 'Lorry', 'cost': 200},
            {'name': 'Barge', 'cost': 220}
        ]
        self.assertEqual(cheapestVehicle.getCheapestVehicle(listOfVehicles), {'name': 'Van', 'cost': 100})

        listOfVehicles = [
            {'name': 'Van', 'cost': 200},
            {'name': 'Lorry', 'cost': 190},
            {'name': 'Barge', 'cost': 220}
        ]
        self.assertEqual(cheapestVehicle.getCheapestVehicle(listOfVehicles), {'name': 'Lorry', 'cost': 190})
        
        listOfVehicles = [
            {'name': 'Van', 'cost': 200},
            {'name': 'Lorry', 'cost': 220},
            {'name': 'Barge', 'cost': 190}
        ]
        self.assertEqual(cheapestVehicle.getCheapestVehicle(listOfVehicles), {'name': 'Barge', 'cost': 190})