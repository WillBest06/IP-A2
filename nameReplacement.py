import pathlib

textFileFolder = pathlib.Path('C:\Temporary Workspace\IP-A2')

listOfFiles = list(textFileFolder.iterdir())
print(listOfFiles)