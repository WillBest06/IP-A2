import cheapestVehicle, unittest

class testCheapestVehicle(unittest.TestCase): 
    def testCalcVanCost(self):
        self.assertEqual(cheapestVehicle.calcVanCost(0), 37)
        self.assertEqual(cheapestVehicle.calcVanCost(100), 47)