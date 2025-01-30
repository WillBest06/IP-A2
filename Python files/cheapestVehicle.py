import time

def getDistance():
    distanceKM = 0

    while not (distanceKM > 0):
        distanceKM = input('\nPlease enter the delivery distance (kilometres): ')

        try: # if a user enters a non float input then it won't cast to int and will ask for another input
            return float(distanceKM)
        except:
            if distanceKM <= 0:
                print('Error: distance must be greater than 0.')
            else:
                print('Error: you may only input numbers.')
            
            distanceKM = 0
            continue

def calcVehicleCost(distance, baseCost, fuelConsumption, oneLitreFuelCost, metricConversionRatio):
    KMLfuelConsumption = fuelConsumption * metricConversionRatio
    
    vehicleTotalCost = baseCost + ((distance / KMLfuelConsumption) * oneLitreFuelCost)

    return round(vehicleTotalCost, 2)

def getCheapestVehicle(vehicles):
    cheapestVehicle = vehicles[0] # initialisation to compare against others

    for currentVehicle in vehicles:
        if currentVehicle['total_cost'] < cheapestVehicle['total_cost']:
            cheapestVehicle = currentVehicle

    return cheapestVehicle

def main():
    ONE_LITRE_FUEL_COST = 1 # price in £

    vehicles = [ # conversion ratio * fuel consumption is fuel consumption in km/l
                {'name': 'Van', 'base_cost_pounds': 37, 'fuel_consumption': 10, 'conversion_ratio': 1}, # consumption in km/l
                {'name': 'Lorry', 'base_cost_pounds': 47, 'fuel_consumption': 53, 'conversion_ratio': 0.354006}, # consumption in mpg
                {'name': 'Barge', 'base_cost_pounds': 47, 'fuel_consumption': 78, 'conversion_ratio': 0.4074} # consumption in nmpg
            ]

    print('\n*** Fuel Calculator V1.0 ***')

    while True:
        print('\nPlease select an option from below:')
        print('1) Cost comparison and cheapest option')
        print("Type 'e' to close the program")
        choice = input('\nYour choice: ')

        if choice.lower() == 'e':
            print('Exiting...')
            time.sleep(1)
            return
        elif choice == '1':
            distance = getDistance()

            for vehicle in vehicles: # creates new key total_cost
                vehicle['total_cost'] = calcVehicleCost(
                    distance, vehicle['base_cost_pounds'], vehicle['fuel_consumption'],
                    ONE_LITRE_FUEL_COST, vehicle['conversion_ratio']
                )
            
            cheapestVehicle = getCheapestVehicle(vehicles)

            # format methods below reference dictionaries containing keys 'name' and 'cost'
            # format was more concise than f strings due to string containing several keys
                
            for vehicle in vehicles:
                print('\n| Vehicle type: {name} | Cost: £{total_cost} |'.format(**vehicle)) 

            print('\nThe cheapest vehicle is {name}, at a cost of £{total_cost}'.format(**cheapestVehicle)) 
            
            time.sleep(10) # provides the user time to read info
        else:
            print('Please choose from the list of options.')
            time.sleep(2)
            continue

if __name__ == "__main__":
    main()