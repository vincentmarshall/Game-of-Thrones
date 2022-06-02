import os
import json


class Job():
    def __init__(self):
        self.name = ""

def importJobs():
    print('Importing Jobs')
    
    data_file = os.getcwd() + '\data\jobs_data.json'
    isEmpty = os.stat(data_file).st_size == 0

    if (isEmpty):
        print('No jobs to import.')
        return

    with open(data_file) as data_file:
        list = json.load(data_file)
    
    return list