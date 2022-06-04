from email.policy import default
import json
import os

char_file = os.getcwd() + '\data\character_data.json'

class Character():

    #Core Character Functions
    def __init__(self, defaultValues = None):
        if defaultValues is None:
            self.name = ""
            self.allegiance = ""
            self.title = ""
            self.location = ""
            self.traits = {
                'strength' : 0,
                'dextarity' : 0,
                'intelligence' : 0,
                'wisdom' : 0,
                'charisma' : 0
            }
        else:
            self.name = defaultValues['name']
            self.allegiance = defaultValues['allegiance']
            self.title = defaultValues['title']
            self.location = defaultValues['location']
            self.traits = defaultValues['traits']

    def save(self):
        isEmpty = os.stat(char_file).st_size == 0
        newCharacter = self.__dict__
        list = []
        if isEmpty:
            list.append(newCharacter)
            with open(char_file, "w") as fp:
                json.dump(list, fp, indent=4)
        else:

            with open(char_file) as data_file:
                list = json.load(data_file)

            list.append(newCharacter)

            with open(char_file, "w") as fp:
                json.dump(list, fp, indent=4)

    def delete(self):
        deleteIndex = None

        with open(char_file) as data_file:
            list = json.load(data_file)

        for index, value in enumerate(list):
            if value['name'] == self.name:
                deleteIndex = index
        
        list.pop(deleteIndex)

        with open(char_file, 'w') as fp:
            json.dump(list, fp, indent=4)
        
        return True

    def update(self, changeVal, newVal):
        changeVal = changeVal.lower()
        toChange = getattr(self, changeVal)
        with open(char_file) as data_file:
            list = json.load(data_file)

        for index, value in enumerate(list):
            if value[changeVal] == toChange:
                dictIndex = index
        
        dictObj = list[dictIndex]
        
        dictObj[changeVal] = newVal

        with open(char_file, "w") as fp:
            json.dump(list, fp, indent=4)

        return True
    
    

    #Supplementary Character Functions

    def isNoble(self):
        print(self.title)
def importCharacters():
    print('Importing Characters')


    isEmpty = os.stat(char_file).st_size == 0

    if (isEmpty):
        print('No characters to import.')
    else:
        fileObject = open(char_file, "r")
        jsonContent = fileObject.read()
        characterList = json.loads(jsonContent)
        newList = []
        for characterData in characterList:
            newcharacter = Character(characterData)
            newList.append(newcharacter)
        return newList
