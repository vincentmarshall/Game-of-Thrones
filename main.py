import house_class
import character_class

houseList = house_class.importHouses()
characterList = character_class.importCharacters()

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

print(f'{bcolors.HEADER}------Welcome to Game of Thrones Character Simulator!------{bcolors.ENDC}')

def MainMenu():
    global houseList
    global characterList
    option = None

    while option == None:

        print(f'{bcolors.BOLD}What would you like to do?\n{bcolors.ENDC}')

        print(f'{bcolors.OKGREEN}[1] Display Noble Houses{bcolors.ENDC}')
        print(f'{bcolors.OKGREEN}[2] Display Characters{bcolors.ENDC}')
        print(f'{bcolors.OKGREEN}[3] Create Noble House{bcolors.ENDC}')
        print(f'{bcolors.OKGREEN}[4] Create Character{bcolors.ENDC}')
        print(f'{bcolors.OKGREEN}[5] Edit House{bcolors.ENDC}')
        print(f'{bcolors.OKGREEN}[6] Edit Character{bcolors.ENDC}')


        print('\n')
        print(f'{bcolors.OKGREEN}[0] Exit{bcolors.ENDC}')

        print('\n')
        print("Please enter your choice")
        option = int(input())

        if option == 0:
            quit()
        if option == 1:

            result = RetrieveHouseNames()

            if result != None:
                print(f'{bcolors.BOLD}Current Houses:{bcolors.ENDC}')

                for names in result:
                    print(names.title())
            
            else:
                print(f'{bcolors.BOLD}There are no houses created yet.{bcolors.ENDC}')

            option = None


        if option == 2:
            result = RetrieveCharacterNames()

            if result != None:
                print(f'{bcolors.BOLD}Current Characters:{bcolors.ENDC}')

                for names in result:
                    print(names.title())
            else:
                print(f'{bcolors.BOLD}There are no characters created yet.{bcolors.ENDC}')

            option = None


        if option == 3:
            newHouse = CreateHouse()
            if houseList:
                houseList.append(newHouse)
            else:
                houseList = []
                houseList.append(newHouse)
            option = None

        if option == 4:
            newChar = CreateCharacter()
            characterList.append(newChar)
            option = None

        if option == 5:

            success = EditHouse()
            if success:
                houseList = house_class.importHouses()
            option = None

        if option == 6:

            success = EditCharacter()
            if success:
                characterList = character_class.importCharacters()

            option = None




    
def RetrieveHouseNames():
    returnMessage = None
    if houseList != None:
        returnMessage = []
        for house in houseList:
            returnMessage.append(house.name)

    return returnMessage
    
def RetrieveCharacterNames():
    returnMessage = None
    if characterList != None:
        returnMessage = []
        for character in characterList:
            returnMessage.append(character.name)

    return returnMessage

def CreateHouse(passedData = None):

    if passedData:
        newHouse = house_class.House()
    
        houseName = passedData[0]
        charName = passedData[1]

        print(f"{bcolors.BOLD}Creating house " + houseName + " {bcolors.ENDC}")

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

        print(f"{bcolors.BOLD}What is house " + houseName + "'s sigil? {bcolors.ENDC}")
        houseSigil = input()

        print(f'{bcolors.BOLD}What seat does house ' + houseName + ' hold? {bcolors.ENDC}')
        houseSeat = input()

        print(f'{bcolors.BOLD}Who is the Lord of house ' + houseName + '? {bcolors.ENDC}')
        houseLord = input()

    newHouse.name = houseName
    newHouse.sigil = houseSigil
    newHouse.seat = houseSeat
    newHouse.lord = houseLord

    newHouse.save()

    return newHouse

def CreateCharacter():
    print("Creating Character")

    houseObj = None
    newCharacter = character_class.Character()

    print(f'{bcolors.BOLD}What is your characters name? {bcolors.ENDC}')
    name = input()

    nameSplit = name.split()
    lastName = nameSplit[1].title()

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
    title = input()


    newCharacter.name = name
    newCharacter.title = title

    newCharacter.save()

    houseObj.updateMembers(newCharacter.name, False)

    return newCharacter

def EditHouse():

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

def DeleteHouse(passedData):
    print("")

def EditCharacter(passedData = None):

    index = 1
    option = None
    optionList = []


    if passedData:
        print('What would you like to edit of ' + passedData.name.title() + '?')
        for value in vars(passedData):
            print('[' + str(index) + '] ' + value.title())
            optionList.append(value.title())
            index = index + 1
        
        option = int(input())

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


        option = int(input())

        if option == 0:

            deleteConfirm = None
            while deleteConfirm != characterEdit.name:
                
                print('Please type ' + characterEdit.name + ' to confirm deletion or [0] to cancel')
                deleteConfirm = input()

                if deleteConfirm == '0':
                    success = False
                    return success
        
            success = characterEdit.delete()
            return success
            
    index = 1


    characterEdit = characterList[option - 1]

    

    toChange = int(input()) - 1

    newName = input("Enter new " + optionList[toChange] + " for " + characterEdit.name + "\n")

    characterObj = [item for item in characterList if item.name == characterEdit.name]

    success = characterObj[0].update(optionList[toChange], newName)


    print('Character Updated')

    return(success)
    



MainMenu()
