import json
import os

data_file = os.getcwd() + ''

class Class:

    def __init__(self):
        print()

    def save(self):

        newClass = self.__dict__
        newList = []
        newList.append(newClass)

        with open(data_file, 'w') as fp:
            json.dump(newList, fp, indent = 4)
