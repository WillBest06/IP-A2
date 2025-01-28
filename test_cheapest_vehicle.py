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
        self.assertEqual(cheapestVehicle.getCheapestVehicle(), )
        self.assertEqual(cheapestVehicle.getCheapestVehicle(), )
        self.assertEqual(cheapestVehicle.getCheapestVehicle(), )

