import os

def getTextFiles():
    folderPath = input('\nPlease enter the path of the folder you wish to open: ')
    os.chdir(folderPath) # files can be manipulated using just their names

    listOfFiles = list(os.listdir(folderPath)) # lists all files in the folder

    textFiles = []

    for file in listOfFiles:
        if str(file).endswith('.txt'): # filters out non-text files
            textFiles.append(file)

    return textFiles

def replaceTextInFile(textFile, searchWord, replacementWord):
    newTextContents = ''

    with open(textFile, 'r') as file:
        textContents = file.read()
        numOfReplacements = textContents.count(searchWord) # instances of word to be replaced

        newTextContents = textContents.replace(searchWord, replacementWord) # does not edit file
        
    with open(textFile, 'w') as file:
        file.write(newTextContents) # overwrites file with text replaced
        

    return numOfReplacements 

def main():  
    try:
        textFiles = getTextFiles()
    except:
        print('\nNo text files were found. Please enter a different folder path.')
        main()

    print(f'\nText files found: {len(textFiles)}')

    searchWord = input('\nWhat word would you like to replace: ')
    replacementWord = input('What word would you like to replace that with: ')
    totalReplacementsMade = 0

    for textFile in textFiles:
        numOfReplacements = replaceTextInFile(textFile, searchWord, replacementWord)
        print(f'\nReplacements made in {textFile}: {numOfReplacements}')
        totalReplacementsMade += numOfReplacements # tracks replacements made across all files

    print(f'Total replacements made: {totalReplacementsMade}')

if __name__ == "__main__":
    main() # doesn't run immediately when imported