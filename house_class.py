from errno import ESTALE
import json
import os
import string

houseDataListFile = 'house_data.json'

class House():

    #Core House functions
    def __init__(self, defaultValues = None):
        if defaultValues is None:
            self.name = ""
            self.sigil = ""
            self.seat = ""
            self.lord = ""
            self.royal = False
            self.members = []
        else:
            self.name = defaultValues['name']
            self.sigil = defaultValues['sigil']
            self.seat = defaultValues['seat']
            self.lord = defaultValues['lord']
            self.members = defaultValues['members']

    def save(self):
        isEmpty = os.stat(houseDataListFile).st_size == 0
        newHouse = self.__dict__
        list = []
        if isEmpty:
            list.append(newHouse)
            with open(houseDataListFile, "w") as fp:
                json.dump(list, fp, indent=4)
        else:

            with open(houseDataListFile) as data_file:
                list = json.load(data_file)

            list.append(newHouse)

            with open(houseDataListFile, "w") as fp:
                json.dump(list, fp, indent=4)
            print('House Saved')

    def delete(self):

        deleteIndex = None

        with open(houseDataListFile) as data_file:
            list = json.load(data_file)
        
        for index, value in enumerate(list):
            if value['name'] == self.name:
                deleteIndex = index
        
        list.pop(deleteIndex)

        with open(houseDataListFile, 'w') as fp:
            json.dump(list, fp, indent=4)

        return True

    def update(self, changeVal, newVal):
        changeVal = changeVal.lower()
        toChange = getattr(self, changeVal)
        with open(houseDataListFile) as data_file:
            list = json.load(data_file)

        for index, value in enumerate(list):
            if value[changeVal] == toChange:
                dictIndex = index
                
        dictObj = list[dictIndex]
        
        dictObj[changeVal] = newVal

        with open(houseDataListFile, "w") as fp:
            json.dump(list, fp, indent=4)

        return True

    #Supplementary House functions
    def updateMembers(self, memberName: string, remove: bool):
        with open(houseDataListFile) as data_file:
            list = json.load(data_file)
        
        if remove:
            print("removing is not set up yet")
        else:
            memberList = self.members
            memberList.append(memberName)

        for value in list:
            if value['name'] == self.name:

                value['members'] = memberList

                print(memberName.title() + " added to house " + self.name)
                break
    
        with open(houseDataListFile, 'w') as fp:
            json.dump(list, fp, indent=4)

def importHouses():
    isEmpty = os.stat(houseDataListFile).st_size == 0

    if (isEmpty):
        print('No houses to import.')
    else:
        fileObject = open("house_data.json", "r")
        jsonContent = fileObject.read()
        houseList = json.loads(jsonContent)
        newList = []
        for houseData in houseList:
            newHouse = House(houseData)
            newList.append(newHouse)
        return newList

