import json
import os

characterDataListFile = 'character_data.json'

class Character():

    #Core Character Functions
    def __init__(self, defaultValues = None):
        if defaultValues is None:
            self.name = ""
            self.allegiance = ""
            self.title = ""
        else:
            self.name = defaultValues['name']
            self.allegiance = defaultValues['allegiance']
            self.title = defaultValues['title']
    def save(self):
        isEmpty = os.stat(characterDataListFile).st_size == 0
        newCharacter = self.__dict__
        list = []
        if isEmpty:
            list.append(newCharacter)
            with open(characterDataListFile, "w") as fp:
                json.dump(list, fp, indent=4)
        else:

            with open(characterDataListFile) as data_file:
                list = json.load(data_file)

            list.append(newCharacter)

            with open(characterDataListFile, "w") as fp:
                json.dump(list, fp, indent=4)
    def delete(self):
        deleteIndex = None

        with open(characterDataListFile) as data_file:
            list = json.load(data_file)

        for index, value in enumerate(list):
            if value['name'] == self.name:
                deleteIndex = index
        
        list.pop(deleteIndex)

        with open(characterDataListFile, 'w') as fp:
            json.dump(list, fp, indent=4)
        
        return True
    def update(self, changeVal, newVal):
        changeVal = changeVal.lower()
        toChange = getattr(self, changeVal)
        with open(characterDataListFile) as data_file:
            list = json.load(data_file)

        for index, value in enumerate(list):
            if value[changeVal] == toChange:
                dictIndex = index
        
        dictObj = list[dictIndex]
        
        dictObj[changeVal] = newVal

        with open(characterDataListFile, "w") as fp:
            json.dump(list, fp, indent=4)

        return True

    #Supplementary Character Functions

    
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
