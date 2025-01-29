import time

def getDistance():
    distanceKM = 0

    while not (distanceKM > 0):
        distanceKM = input('\nPlease enter the delivery distance (kilometres): ')

        try: # if a user enters a non float input then it won't cast to int and will ask for another input
            return float(distanceKM)
        except:
            print('Error: you may only input numbers')
            distanceKM = 0
            continue

def calcVehicleCost(distance, baseCost, fuelConsumption, oneLitreFuelCost, metricConversionRatio):
    KMLfuelConsumption = fuelConsumption * metricConversionRatio
    
    vehicleTotalCost = baseCost + ((distance / KMLfuelConsumption) * oneLitreFuelCost)

    return round(vehicleTotalCost, 2)

def getCheapestVehicle(listOfVehicles):
    cheapestVehicle = listOfVehicles[0] # initialises with the 1st value to compare against the others

    for currentVehicle in listOfVehicles:
        if currentVehicle['cost'] < cheapestVehicle['cost']:
            cheapestVehicle = currentVehicle

    return cheapestVehicle

def main():
    ONE_LITRE_FUEL_COST = 1 # price in £

    VAN_BASE_COST = 37  # price in £
    VAN_FUEL_CONSUMPTION = 10 # kilometres/Litre
    VAN_KML_TO_KML_RATIO = 1

    LORRY_BASE_COST = 47  # price in £
    LORRY_FUEL_CONSUMPTION_MPG = 53 # miles/gallon
    LORRY_MPG_TO_KML_RATIO = 0.354006

    BARGE_BASE_COST = 47  # price in £
    BARGE_FUEL_CONSUMPTION_NMPG = 53 # nautical miles/gallon
    BARGE_NMPG_TO_KML_RATIO = 0.4074

    print('\n*** Fuel Calculator V1.0 ***')

    while True:
        print('\nPlease select an option from below:')
        print('1) Cost comparison and cheapest option')
        print("Type 'e' to close the program")
        choice = input('\nYour choice: ')

        if choice.lower() == 'e':
            return
        elif int(choice) == 1:
            distance = getDistance()
            vanCost = calcVehicleCost(distance, VAN_BASE_COST, VAN_FUEL_CONSUMPTION, ONE_LITRE_FUEL_COST, VAN_KML_TO_KML_RATIO)
            lorryCost = calcVehicleCost(distance, LORRY_BASE_COST, LORRY_FUEL_CONSUMPTION_MPG, ONE_LITRE_FUEL_COST, LORRY_MPG_TO_KML_RATIO)
            bargeCost = calcVehicleCost(distance, BARGE_BASE_COST, BARGE_FUEL_CONSUMPTION_NMPG, ONE_LITRE_FUEL_COST, BARGE_NMPG_TO_KML_RATIO )

            van = {
                'name': 'Van',
                'cost': vanCost
            }

            lorry = {
                'name': 'Lorry',
                'cost': lorryCost
            }

            barge = {
                'name': 'Barge',
                'cost': bargeCost
            }
            
            listOfVehicles = [van, lorry, barge] # list of dictionaries
            cheapestVehicle = getCheapestVehicle(listOfVehicles)

            # format methods below reference dictionaries containing keys 'name' and 'cost'
            # format was more concise than f strings due to string containing several keys
                
            for vehicle in listOfVehicles:
                print('\n| Vehicle type: {name} | Cost: £{cost} |'.format(**vehicle)) 

            print('\nThe cheapest vehicle is {name}, at a cost of £{cost}'.format(**cheapestVehicle)) 
            
            time.sleep(10) # provides the user time to read info
        else:
            print('Please choose from the list of options.')
            time.sleep(2)
            continue

if __name__ == "__main__":
    main()