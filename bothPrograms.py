import cheapestVehicle, wordReplacement

print('Select an option:')
print('1) Find the cheapest transport vehicle')
print('2) Replace words in text files')

choice = int(input('Choice: '))

if choice == 1:
    cheapestVehicle.main()
elif choice == 2:
    wordReplacement.main()
else:
    print('Error')