import json

classDataListFile = 'class_data.json'

class Class:

    def __init__(self):
        print()

    def save(self):

        newClass = self.__dict__
        newList = []
        newList.append(newClass)

        with open(classDataListFile, 'w') as fp:
            json.dump(newList, fp, indent = 4)
