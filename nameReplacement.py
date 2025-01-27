import os

def getTextFiles():
    folderPath = input('Please enter the path of the folder you wish to open: ')
    os.chdir(folderPath)

    listOfFiles = list(os.listdir(folderPath))

    textFiles = []

    for file in listOfFiles:
        if str(file).endswith('.txt'):
            textFiles.append(file)
    
    return textFiles

def replaceTextInFile(textFile, searchWord, replacementWord):
    newTextContents = ''

    with open(textFile, 'r') as file:
        textContents = file.read()
        numOfReplacements = textContents.count(searchWord)

        newTextContents = textContents.replace(searchWord, replacementWord)
        
    with open(textFile, 'w') as file:
        file.write(newTextContents)
        

    return numOfReplacements

def main():   
    textFiles = getTextFiles()

    print(f'Number of files with .txt extension: {len(textFiles)}')

    searchWord = input('What word would you like to replace: ')
    replacementWord = input('What word would you like to replace that with: ')
    totalReplacementsMade = 0

    for textFile in textFiles:
        numOfReplacements = replaceTextInFile(textFile, searchWord, replacementWord)
        print(f'Replacements made: {numOfReplacements}')
        totalReplacementsMade += numOfReplacements

main()