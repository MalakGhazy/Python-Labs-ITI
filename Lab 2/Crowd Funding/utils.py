import json
import os

def load_data(file):
    '''Load data from a JSON file.'''
    if os.path.exists(file):
        with open(file,"r") as f: # Open the file in read mode
            return json.load(f) # Convert JSON content into a Python object (list/dictionary)
    return[] # Return an empty list if the file does not exist

def save_data(file,data):
    with open(file,"w") as f:
        json.dump(data,f,indent=4) # Convert Python object to JSON and save
        # indent=4 makes the JSON file nicely formatted (readable).