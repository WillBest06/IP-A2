import cheapestVehicle, unittest

class testCheapestVehicle(unittest.TestCase):
    def testCalcVanCost(self):
        self.assertEqual(cheapestVehicle.calcVanCost(0), 37)
        self.assertEqual(cheapestVehicle.calcVanCost(100), 47)
        self.assertEqual(cheapestVehicle.calcVanCost(100.44), 47.04)

    def testCalcLorryCost(self):
        self.assertEqual(cheapestVehicle.calcLorryCost(0), 47)
        self.assertEqual(cheapestVehicle.calcLorryCost(100), 52.33)
        self.assertEqual(cheapestVehicle.calcLorryCost(100.44), 52.35)

    def testBargeLorryCost(self):
        self.assertEqual(cheapestVehicle.calcBargeCost(0), 47)
        self.assertEqual(cheapestVehicle.calcBargeCost(100), 51.63)
        self.assertEqual(cheapestVehicle.calcBargeCost(100.44), 51.65)

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