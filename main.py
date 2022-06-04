from webbrowser import get
import os

from attr import attr

from functions import house_class
from functions import character_class
from functions import jobs_class
from functions import place_class

houseList = house_class.importHouses()
characterList = character_class.importCharacters()
jobsList = jobs_class.importJobs()
placeList = place_class.ImportPlaces()

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

houseDataListFile = 'house_data.json'

userCharacter = None

print(f'{bcolors.HEADER}------Welcome to Game of Thrones Character Simulator!------\n{bcolors.ENDC}')

def MainMenu():
    global houseList
    global characterList
    optionInput = None

    optionList = [
        
        {'name': 'Display Houses', 'active': True, 'func': PrintHouseNames},
        {'name': 'Display Characters','active': True, 'func': PrintCharacterNames},
        {'name': 'Select Character','active': True, 'func': SelectCharacter},
        {'name': 'ADMIN MENU','active': True, 'func': AdminMenu},
        
    ]

    while optionInput == None:

        print(f'{bcolors.OKCYAN}-----------------MAIN MENU-----------------\n{bcolors.ENDC}')
        print(f'{bcolors.BOLD}What would you like to do?\n{bcolors.ENDC}')

        for index, value in enumerate(optionList):
            print( "[" + str(index + 1) + "] " + str(value['name']))

        print(f'{bcolors.OKGREEN}\n[0] Exit{bcolors.ENDC}')

        print('\n')
        print("Please enter your choice")
        optionInput = int(input())

        optionList[optionInput - 1]['func']()

def GameMenu():

    ClearConsole()

    global userCharacter

    optionList = [
        {'name': 'Display Houses', 'active': True, 'func': PrintHouseNames},
        {'name': 'Display Characters','active': True, 'func': PrintCharacterNames},
        {'name': 'Select Character','active': True, 'func': SelectCharacter},
        {'name': 'ADMIN MENU','active': True, 'func': AdminMenu},        
    ]

    if userCharacter:
        print('You are currently ' + userCharacter.name)
    else:
        SelectCharacter()

    print(f'{bcolors.OKCYAN}-----------------GAME MENU-----------------\n{bcolors.ENDC}')
    print(f'{bcolors.BOLD}What would you like to do?\n{bcolors.ENDC}')

def SelectCharacter():

    global userCharacter

    #PrintCharacterNames()

    print('Which character would you like to select?')
    for index, character in enumerate(characterList):
        print('[' + str(index + 1) + '] ' + character.name)
        for trait in character.traits:
            print('   |_ ' + trait + ': ' + str(character.traits[trait]))
    optionInput = input()

    userCharacter = characterList[int(optionInput) - 1]

    GameMenu()

def AdminMenu():

    ClearConsole()

    option = None

    optionList = [
        
        {'name': 'Create House','active': True, 'func': CreateHouse},
        {'name': 'Create Character','active': True, 'func': CreateCharacter},
        {'name': 'Create Place','active': True, 'func': CreatePlace},
        {'name': 'Display Places','active': True, 'func': PrintPlaces},
        {'name': 'Edit House','active': True, 'func': EditHouse},
        {'name': 'Edit Character','active': True, 'func': EditCharacter},
        
    ]

    while option == None:

        print(f'{bcolors.OKCYAN}-----------------ADMIN MENU-----------------\n{bcolors.ENDC}')
        print(f'{bcolors.BOLD}What would you like to do?\n{bcolors.ENDC}')

        for index, value in enumerate(optionList):
            print( "[" + str(index + 1) + "] " + str(value['name']))

        print(f'{bcolors.OKGREEN}\n[/] Back{bcolors.ENDC}')
        print(f'{bcolors.OKGREEN}\n[0] Exit{bcolors.ENDC}')

        print('\n')
        print("Please enter your choice")
        optionInput = input()
        if optionInput == "/":
            ClearConsole()
            MainMenu()
        elif optionInput == "0":
            quit()
        optionList[int(optionInput) - 1]['func']()

def PrintHouseNames():

    ClearConsole()

    if houseList != None:
        for house in houseList:
            print(house.name.title())
            print('|_ ' + 'Members:')
            if len(house.members) == 0:
                print('   There are no members')
            else:
                for member in house.members:
                    print('  |_' + member)
    else:
        print('There are no houses created yet.')

    return
    
def PrintCharacterNames():

    ClearConsole()

    if characterList != None:
        for character in characterList:
            print(character.name.title())
            for trait in character.traits:
                print('|_ ' + trait + ': ' + str(character.traits[trait]))

            print('\n')
    else:
        print('There are no characters created yet.')

    MainMenu()

def PrintPlaces():

    ClearConsole()

    if placeList != None:
        for place in placeList:
            print(place.name.title())
    else:
        print("There are no places created yet.")

def CreatePlace(passedData = None):

    global placeList

    ClearConsole()

    newPlace = place_class.Place()

    if passedData:
        print('not set up yet')
        name = passedData["name"]
        rulers = passedData["rulers"]
        print("Where is " + name)
        location = input()
    else:

        print("What is the name of the place?")
        name = input()
        print("Who are rulers of " + name)
        rulers = input()
        print("Where is " + name)
        location = input()



    newPlace.name = name
    newPlace.rulers = rulers
    newPlace.location = location
    newPlace.save()

    if placeList:
        placeList.append(newPlace)
    else:
        placeList = []
        placeList.append(newPlace)

    return newPlace

def CreateHouse(passedData = None):

    global houseList

    ClearConsole()


    if passedData:
        newHouse = house_class.House()
    
        houseName = passedData[0]
        charName = passedData[1]

        print(f'{bcolors.BOLD}Creating house ' + houseName + '{bcolors.ENDC}')

        print(f'{bcolors.BOLD}Is ' + charName + ' the Lord of house ' + houseName + '? {bcolors.ENDC}')
        yesNo = input().lower()

        if yesNo == 'yes' or yesNo == 'y':
            houseLord = charName
        else:
            print(f'{bcolors.BOLD}Who is the Lord of house ' + houseName + '? {bcolors.ENDC}')
            houseLord = input()
        
        print(f"{bcolors.BOLD}What is house " + houseName + "'s sigil? {bcolors.ENDC}")
        houseSigil = input()

        print(f'{bcolors.BOLD}What seat does house ' + houseName + ' hold? {bcolors.ENDC}')
        houseSeat = input()
        
    else:
        newHouse = house_class.House()

        print(f'{bcolors.BOLD}Please enter a house name to create. {bcolors.ENDC}')
        houseName = input()

        if houseList:
            for house in houseList:
                if (house.name.title() == houseName.title()):
                    print('House ' + houseName + ' already exists, please choose another name.')
                    CreateHouse()

        print(f"{bcolors.BOLD}Creating house " + houseName + " {bcolors.ENDC}")

        print('Is ' + houseName + ' a Royal House?')
        userInput = input()
        if userInput.lower() == 'y' or userInput.lower() == 'yes':
            royal = True
        else:
            royal = False

        print(f"{bcolors.BOLD}What is house " + houseName + "'s sigil? {bcolors.ENDC}")
        houseSigil = input()
        print(f'{bcolors.BOLD}What seat does house ' + houseName + ' hold? {bcolors.ENDC}')
        seatInput = input()


        #Find place to assign from list
        houseSeat = None
        for place in placeList:
            if place.name == seatInput:
                houseSeat = place.name
                break
    
        #If no place exists, prompt for creation
        if not houseSeat:
            print(seatInput + " does not exist, would you like to create it?")
            yesNo = input()
            if yesNo.lower() == 'yes' or yesNo.lower() == 'y':
                #Assign house seat to the newly created house
                newPlace = CreatePlace({"name": seatInput, "rulers": houseName})
                houseSeat = newPlace.name
            else:
                houseSeat = "Unknown"


        #Find all noble characters with the house name
        nobleList = []
        for character in characterList:
            nameSplit = character.name.split()
            lastName = nameSplit[1]
            if lastName.lower() == houseName.lower():
                nobleList.append(character)

        #Print all characters in noble list with last name of house, if any

        print(f'{bcolors.BOLD}Who is the Lord of house ' + houseName + '? {bcolors.ENDC}')
        if len(nobleList) == 0:
            print("No current characters belong to this house")
            houseLord = input()
        else:
            for index, character in enumerate(nobleList):
                print('[' + str(index + 1) + '] ' + character.name.title())
            userInput = input()
            houseLord = nobleList[int(userInput) - 1].name


    #Output values into object
    newHouse.name = houseName
    newHouse.royal = royal
    newHouse.sigil = houseSigil
    newHouse.seat = houseSeat
    newHouse.lord = houseLord

    #Save object to file
    newHouse.save()

    #Append new house to local list
    if houseList:
        houseList.append(newHouse)
    else:
        houseList = []
        houseList.append(newHouse)

    return

def CreateCharacter():

    ClearConsole()


    print("Creating Character")

    houseObj = None
    newCharacter = character_class.Character()

    print(f'{bcolors.BOLD}What is your characters name? {bcolors.ENDC}')
    name = input()

    nameSplit = name.split()
    if len(nameSplit) < 2:
        print('Please give your character a last name.')
        lastName = input()
        name = name + " " + lastName
    else:
        lastName = nameSplit[1].title()

    if characterList:
        for character in characterList:
            if character.name == name:
                print("Character already exists, would you like to edit " + name.title() + "?")
                yesNo = input()

                if yesNo == "yes" or yesNo =='y':
                    EditCharacter(character)

                break

    for house in houseList:
        if house.name == lastName:
            houseObj = house
            break

    if not houseObj:
        print("No house exits for the character being created.")
        print("Would you like to create house " + lastName.title() + "?")
        yesNo = input().lower()
        if yesNo == 'yes' or yesNo == 'y':
            passData = [lastName, name]
            houseObj = CreateHouse(passData)
        else:
            print(name + " will be assigned to freelancers")
            for house in houseList:
                if house.name == 'Freelancers':
                    houseObj = house
                    break

    print(f'{bcolors.BOLD}What title does ' + name + ' hold? {bcolors.ENDC}')
    for index, job in enumerate(jobsList):
        print('[' + str(index + 1) + '] ' + job["title"])

    userInput = input()
    title = jobsList[int(userInput) - 1]

    print(f'{bcolors.BOLD}Where is ' + name + ' currently?{bcolors.ENDC}')

    ClearConsole()

    pointsLeft = 120
    print('You have been given 200 attribute points for your character, spend wisely!')


    valueList = []
    while pointsLeft > 0:
        print('What would you like to assign points to?')
        print('You have ' + str(pointsLeft) + ' points left\n')
        for index, (trait, value) in enumerate(newCharacter.traits.items()):
            print('[' + str(index + 1) + '] ' + str(trait.title()) + '     ' + str(value))
            valueList.append(trait)

        userChoice = input()

        print('How many points would you like to assign ' + valueList[int(userChoice) - 1] + '?')
        userAmmount = input()
        userAmmount = int(userAmmount)

        choice = valueList[int(userChoice) - 1]

        newCharacter.traits[choice] = userAmmount
        pointsLeft = pointsLeft - userAmmount

    newCharacter.name = name
    newCharacter.title = title

    newCharacter.save()

    houseObj.updateMembers(newCharacter.name, False)
    characterList.append(newCharacter)

    return newCharacter

def EditHouse():

    ClearConsole()

    index = 1
    option = None

    print('Which house would you like to edit?')
    for house in houseList:
        print('[' + str(index) + '] ' + house.name)
        index = index + 1


    index = 1

    option = int(input())
    optionList = []


    houseEdit = houseList[option - 1]

    print('What would you like to edit of house ' + houseEdit.name + '?')
    for value in vars(houseEdit):
        print('[' + str(index) + '] ' + value.title())
        optionList.append(value.title())
        index = index + 1

    print('\n[0] DELETE HOUSE')

    toChange = int(input()) - 1

    if(toChange == -1):

        #print('This will delete all characters assigned to house ' + houseEdit.name)
        print('Please type ' + houseEdit.name + ' to confirm deletion or [0] to cancel')

        confirmInput = ''

        while(confirmInput != houseEdit.name):
            confirmInput = input()
            if confirmInput == houseEdit.name:
                success = houseEdit.delete()
            elif confirmInput == '0':
                success = False
                break
            else:
                print('Please type ' + houseEdit.name + ' to confirm deletion or [0] to cancel')
    else:
        newName = input("Enter new " + optionList[toChange] + " for house " + houseEdit.name + "\n")

        houseObj = [item for item in houseList if item.name == houseEdit.name]

        success = houseObj[0].update(optionList[toChange], newName)


        print('House Updated')

    return(success)

def EditCharacter(passedData = None):

    ClearConsole()

    index = 1
    #option = None
    optionList = []


    if passedData:
        print('What would you like to edit of ' + passedData.name.title() + '?')
        for value in vars(passedData):
            print('[' + str(index) + '] ' + value.title())
            optionList.append(value.title())
            index = index + 1
        
        userOption = int(input())

    else:

        print('Which character would you like to edit?')
        for character in characterList:
            print('[' + str(index) + '] ' + character.name)
            index = index + 1

        option = int(input())
        characterEdit = characterList[option - 1]

        index = 1

        print('What would you like to edit of ' + characterEdit.name.title() + '?')
        for value in vars(characterEdit):
            print('[' + str(index) + '] ' + value.title())
            optionList.append(value.title())
            index = index + 1

        print('\n[0] DELETE CHARACTER')


        userOption = input()

        if int(userOption) == 0:

            deleteConfirm = None
            while deleteConfirm != characterEdit.name:
                
                print('Please type ' + characterEdit.name + ' to confirm deletion or [0] to cancel')
                deleteConfirm = input()

                if deleteConfirm == '0':
                    return False
        
            success = characterEdit.delete()
    
            if success:
                #Delete from local list
                for index, value in enumerate(characterList):
                    if value.name == characterEdit.name:
                        characterList.pop(index)

                #Delete from house members list
                nameSplit = characterEdit.name.split()
                for house in houseList:
                    if str(house.name.lower()) == str(nameSplit[1].lower()):
                        charHouse = house
                
                charHouse.updateMembers(memberName = characterEdit.name, remove = True)
                
            return success
            
    index = 1

    toChange = int(userOption) - 1

    characterEdit = characterList[toChange - 1]

    newName = input("Enter new " + optionList[toChange] + " for " + characterEdit.name + "\n")

    characterObj = [item for item in characterList if item.name == characterEdit.name]

    success = characterObj[0].update(optionList[toChange], newName)


    print('Character Updated')

    return(success)
    
def CreateClass():
    
    ClearConsole()

    print('What class would you like to create?')

def ClearConsole():
    os.system('cls' if os.name == 'nt' else 'clear')
    return

MainMenu()
