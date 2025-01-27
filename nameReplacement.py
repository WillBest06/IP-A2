import pathlib

def getListOfFilesFromFolder():
    folderPath = input('Please enter the path of the folder you wish to open: ')
    textFileFolder = pathlib.Path(folderPath)

    listOfFiles = list(textFileFolder.iterdir())
    
    return listOfFiles



def filterForTextFiles(listOfFiles):
    listOfTextFiles = []

    for file in listOfFiles:
        if file.suffix == '.txt':
            listOfTextFiles.append(file)
        else:
            continue

    return listOfTextFiles

def main():
    l = getListOfFilesFromFolder()

    numberOfTextFiles = len(filterForTextFiles(l))
    print(numberOfTextFiles)

main()
    