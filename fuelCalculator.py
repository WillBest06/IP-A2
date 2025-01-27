import sys, time

def getDistance():
    distanceKM = 0

    while not (distanceKM > 0):
        distanceKM = input('\nPlease enter the delivery distance (kilometres): ')

        try: # if a user enters a non integer input then it won't cast to int and will ask for another input
            return int(distanceKM)
        except:
            print('Error: you may only input numbers')
            distanceKM = 0
            continue

def calcVanCost(distance):
    VAN_BASE_COST = 37  # price in £
    VAN_FUEL_CONSUMPTION = 10 # kilometres/Litre
    ONE_LITRE_FUEL_COST = 1 # price in £

    vanTotalCost = VAN_BASE_COST + ( (distance / VAN_FUEL_CONSUMPTION) * ONE_LITRE_FUEL_COST )
    
    return round(vanTotalCost, 2) # rounded to 2dp for pound sterling

def calcLorryCost(distance):
    LORRY_BASE_COST = 47  # price in £
    LORRY_FUEL_CONSUMPTION_MPG = 53 # miles/gallon
    ONE_LITRE_FUEL_COST = 1 # price in £
    MPG_TO_KML_RATIO = 0.354006

    lorryFuelConsumptionKML = (LORRY_FUEL_CONSUMPTION_MPG * MPG_TO_KML_RATIO)

    lorryTotalCost = LORRY_BASE_COST + ( (distance / lorryFuelConsumptionKML) * ONE_LITRE_FUEL_COST )
    
    return round(lorryTotalCost, 2) # rounded to 2dp for pound sterling

def calcBargeCost(distance):
    BARGE_BASE_COST = 47  # price in £
    BARGE_FUEL_CONSUMPTION_NMPG = 53 # nautical miles/gallon
    ONE_LITRE_FUEL_COST = 1 # price in £
    NMPG_TO_KML_RATIO = 0.4074

    bargeFuelConsumptionKML = (BARGE_FUEL_CONSUMPTION_NMPG * NMPG_TO_KML_RATIO)

    bargeTotalCost = BARGE_BASE_COST + ( (distance / bargeFuelConsumptionKML) * ONE_LITRE_FUEL_COST )
    
    return round(bargeTotalCost, 2) # rounded to 2dp for pound sterling

def getCheapestVehicle(listOfVehicles):
    cheapestVehicle = listOfVehicles[0] # initialises with the 1st value to compare against the others

    for currentVehicle in listOfVehicles:
        if currentVehicle['cost'] < cheapestVehicle['cost']:
            cheapestVehicle = currentVehicle

    return cheapestVehicle

def main():
    print('\n*** Fuel Calculator V1.0 ***')

    while True:
        print('\nPlease select an option from below:')
        print('1) Find the cheapest cost')
        print('2) Compare costs')
        print('3) Comparison and cheapest option')
        print("Type 'e' to close the program")
        choice = input('\nYour choice: ')

        if choice == 'e' or choice == 'E':
            sys.exit(0)

        distance = getDistance()
        vanCost = calcVanCost(distance)
        lorryCost = calcLorryCost(distance)
        bargeCost = calcBargeCost(distance)

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
        if int(choice) == 1:
            print('\nThe cheapest vehicle is {name}, at a cost of £{cost}'.format(**cheapestVehicle)) 
            for vehicle in listOfVehicles:
                print('\n| Vehicle type: {name} | Cost: £{cost} |'.format(**vehicle)) 
        elif int(choice) == 3:
            for vehicle in listOfVehicles:
                print('\n| Vehicle type: {name} | Cost: £{cost} |'.format(**vehicle)) 

            print('\nThe cheapest vehicle is {name}, at a cost of £{cost}'.format(**cheapestVehicle)) 
        
        time.sleep(10) # provides the user time to read info
main()