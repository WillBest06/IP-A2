import fuelCalculator, nameReplacement

print('Select an option:')
print('1) fuel calculator')
print('2) word replacement')

choice = int(input('Choice: '))

if choice == 1:
    fuelCalculator.main()
elif choice == 2:
    nameReplacement.main()
else:
    print('Error')