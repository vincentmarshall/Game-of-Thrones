import json
import os

import house_class

houseList = []

houseDataListFile = 'house_data.json'

houseList = house_class.importHouses()
print("current house list")
#print(houseList)
#####################

print("Welcome to Game of Thrones Character Simulator!")


def CreateHousePrompt():

    print("Would you like to create a house?")
    yesNo = input()
    if yesNo == "yes":
        CreateHouse()
    else:
        CreateHousePrompt()

def CreateHouse():

    newHouse = house_class.House()

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






