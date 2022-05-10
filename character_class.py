import json
import os

characterDataListFile = 'character_data.json'

class Character():

    def __init__(self, defaultValues = None):
        if defaultValues is None:
            self.name = ""
            self.allegiance = ""
            self.title = ""
        else:
            self.name = defaultValues['name']
            self.allegiance = defaultValues['allegiance']
            self.title = defaultValues['title']
    def changeAll(self, name, allegiance, title):
        self.name = name
        self.allegiance = allegiance
        self.title = title
    def changeName(self, newName):
        self.name = newName
    def toDict(self):
        characterDict = self.__dict__
        return characterDict
    def save(self):
        isEmpty = os.stat(characterDataListFile).st_size == 0
        newCharacter = self.__dict__
        list = []
        if isEmpty:
            list.append(newCharacter)
            with open(characterDataListFile, "w") as fp:
                json.dump(list, fp)
        else:

            with open(characterDataListFile) as data_file:
                list = json.load(data_file)

            list.append(newCharacter)

            with open(characterDataListFile, "w") as fp:
                json.dump(list, fp)
            print('character Saved')
    def update(self, changeVal, newVal):
            changeVal = changeVal.lower()
            with open(characterDataListFile) as data_file:
                list = json.load(data_file)
            dictObj = next((i for i, house in enumerate(list) if (house[changeVal] == getattr(self, changeVal), None)))
            dictObj = list[dictObj]
            
            dictObj[changeVal] = newVal

            with open(characterDataListFile, "w") as fp:
                json.dump(list, fp, indent=4)

            return True
    
def importCharacters():
    print('Importing Characters')
    isEmpty = os.stat(characterDataListFile).st_size == 0

    if (isEmpty):
        print('No characters to import.')
    else:
        fileObject = open(characterDataListFile, "r")
        jsonContent = fileObject.read()
        characterList = json.loads(jsonContent)
        newList = []
        for characterData in characterList:
            newcharacter = Character(characterData)
            newList.append(newcharacter)
        return newList
