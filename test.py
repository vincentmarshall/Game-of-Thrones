import json
import os

houseList = []

houseDataListFile = 'house_data.json'

isEmpty = os.stat(houseDataListFile).st_size == 0

if isEmpty:

    fileObject = open("house_data.json", "r")
    jsonContent = fileObject.read()
    houseList = json.loads(jsonContent)


print("current house list")
print(houseList)

class House():

    def __init__(self):
        self.name = ""
        self.sigil = ""
        self.seat = ""
        self.lord = ""
    def changeAll(self, name, sigil, seat, lord):
        self.name = name
        self.sigil = sigil
        self.seat = seat
        self.lord = lord
    def changeName(self, newName):
        self.name = newName
    def toDict(self):
        houseDict = self.__dict__
        return houseDict
    def save(self):
        houseDict = self.__dict__

        with open(houseDataListFile, "r") as fp:
            oldList = json.load(fp)

        print(oldList)
        newList = [oldList]
        newList.append(houseDict)

        print(newList)

        with open(houseDataListFile, "w") as fp:
            json.dump(newList, fp)


        jsonString = json.dumps(houseDict)
        jsonFile = open('house_data.json', 'w')
        jsonFile.write(jsonString)
        jsonFile.close()
        print('House Saved')


print("Welcome to Game of Thrones Character Simulator!")


def CreateHousePrompt():

    print("Would you like to create a house?")
    yesNo = input()
    if yesNo == "yes":
        CreateHouse()
    else:
        CreateHousePrompt()

def CreateHouse():

    newHouse = House()

    print("Please enter a house name to create.")
    houseName = input()

    print("Creating house " + houseName)

    print("What is house " + houseName + "'s sigil?")
    houseSigil = input()

    print("What seat does house " + houseName + " hold?")
    houseSeat = input()

    print("Who is the Lord of house " + houseName + "?")
    houseLord = input()

    newHouse.name = houseName
    newHouse.sigil = houseSigil
    newHouse.seat = houseSeat
    newHouse.lord = houseLord

    newHouse.save()

    CreateHousePrompt()





CreateHousePrompt()






