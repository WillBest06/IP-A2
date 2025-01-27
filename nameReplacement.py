import os

def getListOfFilesFromFolder():
    folderPath = input('Please enter the path of the folder you wish to open: ')
    os.chdir(folderPath)

    listOfFiles = list(os.listdir(folderPath))
    
    return listOfFiles

def filterForTextFiles(listOfFiles):
    listOfTextFiles = []

    for file in listOfFiles:
        if str(file).endswith('.txt'):
            listOfTextFiles.append(file)

    return listOfTextFiles

def replaceTextInFile(textDoc, searchWord, replacementWord):
    with open(textDoc, 'r+') as file:
        textContents = file.read()
        numOfReplacements = textContents.count(searchWord)

        newTextContents = textContents.replace(searchWord, replacementWord)
        file.write(newTextContents)
        

    return numOfReplacements

def main():
    fileList = getListOfFilesFromFolder()
    
    listOfTextFiles = filterForTextFiles(fileList)

    print(f'Number of files with .txt extension: {len(listOfTextFiles)}')

    searchWord = input('What word would you like to replace: ')
    replacementWord = input('What word would you like to replace that with: ')
    totalReplacementsMade = 0

    for textFile in listOfTextFiles:
        numOfReplacements = replaceTextInFile(textFile, searchWord, replacementWord)
        print(f'Replacements made: {numOfReplacements}')
        totalReplacementsMade += numOfReplacements

    
main()

