import house_class

houseList = house_class.importHouses()

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
    option = None
    while option == None:

        print(f'{bcolors.BOLD}What would you like to do?\n{bcolors.ENDC}')

        print(f'{bcolors.OKGREEN}[1] Display Noble Houses{bcolors.ENDC}')
        print(f'{bcolors.FAIL}[2] Display Characters{bcolors.ENDC}')
        print(f'{bcolors.OKGREEN}[3] Create Noble House{bcolors.ENDC}')
        print(f'{bcolors.FAIL}[4] Create Character{bcolors.ENDC}')

        print('\n')
        print(f'{bcolors.OKGREEN}[0] Exit{bcolors.ENDC}')

        print('\n')
        print("Please enter your choice")
        option = int(input())

        if option == 0:
            quit()
        if option == 1:
            result = RetrieveHouseNames()

            print(f'{bcolors.BOLD}Current Houses:{bcolors.ENDC}')
            for names in result:
                print(names.title())
            
            option = None
        if option == 2:
            print()
        if option == 3:
            CreateHouse()



    
def RetrieveHouseNames():
    if houseList == None:
        returnMessage = "There are no houses created yet."
    else:
        returnMessage = []
        for house in houseList:
            returnMessage.append(house.name)

    return returnMessage

# def CreateHousePrompt():

#     print("Would you like to create a house?")
#     yesNo = input().lower()
#     if yesNo == "yes" or yesNo == "y":
#         CreateHouse()
#     else:
#         CreateHousePrompt()

def CreateHouse():

    newHouse = house_class.House()

    print(f'{bcolors.BOLD}Please enter a house name to create. {bcolors.ENDC}')
    houseName = input()

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

    MainMenu()





MainMenu()






