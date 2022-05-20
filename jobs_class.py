import os
import json

jobDataListFile = 'jobs_data.json'

class Job():
    def __init__(self):
        self.name = ""

def importJobs():
    print('Importing Jobs')
    isEmpty = os.stat(jobDataListFile).st_size == 0

    if (isEmpty):
        print('No jobs to import.')
        return

    with open(jobDataListFile) as data_file:
        list = json.load(data_file)
    
    return list