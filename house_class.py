import json
import os

houseDataListFile = 'house_data.json'

class House():

    def __init__(self, defaultValues = None):
        if defaultValues is None:
            self.name = ""
            self.sigil = ""
            self.seat = ""
            self.lord = ""
        else:
            self.name = defaultValues['name']
            self.sigil = defaultValues['sigil']
            self.seat = defaultValues['seat']
            self.lord = defaultValues['lord']
    def changeAll(self, name, sigil, seat, lord):
        self.name = name
        self.sigil = sigil
        self.seat = seat
        self.lord = lord
    def changeValue(self, changeVal, newVal):
        ####self.chnageVal = getattr()
        self.update()
    def toDict(self):
        houseDict = self.__dict__
        return houseDict
    
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
    def update(self):
        print('updating obj')
        print(vars(self))
        with open(houseDataListFile) as data_file:
            list = json.load(data_file)
        dictObj = next((i for i, house in enumerate(list) if house['name'] == self.name), None)
        dictObj = list[dictObj]
        print(dictObj['name'])
        #print(list)
    

def importHouses():
    print('Importing Houses')
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
