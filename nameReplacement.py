import pathlib

def getListOfFilesFromFolder():
    folderPath = input('Please enter the path of the folder you wish to open:')
    textFileFolder = pathlib.Path(folderPath)

    listOfFiles = list(textFileFolder.iterdir())
    
    return listOfFiles

l = getListOfFilesFromFolder()
print(l)