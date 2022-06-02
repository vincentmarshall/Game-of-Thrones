import json
import os

places_file = os.getcwd() + '\data\place_data.json'

class Place():
	def __init__(self, defaultValues = None):
		if defaultValues is None:
				
			self.name = ""
			self.rulers = ""
			self.location = ""
		else:
			self.name = defaultValues['name']
			self.rulers = defaultValues['rulers']
			self.location = defaultValues['location']
	def save(self):
		isEmpty = os.stat(places_file).st_size == 0
		newPlace = self.__dict__
		list = []
		if isEmpty:
			list.append(newPlace)
			with open(places_file, "w") as fp:
				json.dump(list, fp, indent=4)
		else:
			with open(places_file) as data_file:
				list = json.load(data_file)
			
			list.append(newPlace)

			with open(places_file, "w") as fp:
				json.dump(list, fp, indent=4)
			print("Place Saved")
	
def ImportPlaces():
	isEmpty = os.stat(places_file).st_size == 0

	if isEmpty:
		print('No places to import')
	else:
		fileObject = open(places_file, "r")
		jsonContent = fileObject.read()
		placeList = json.loads(jsonContent)
		newList = []
		for houseData in placeList:
			newPlace = Place(houseData)
			newList.append(newPlace)
		return newList


