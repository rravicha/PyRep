
import requests
import json
from pprint import pprint

    data = json.load(open("C:\\Mohan"))

    rul = "www.twitter.com/profile"
    

    #Method to POST input json onto the path
    response_data = requests.post(rul,json=data).json()

    #Output of the Data in json Format
    print(response_data)

    #Printing the output data in proper format
     pprint(response_data)

    #Writing the obtained file into Json
    with open(location2, 'w') as outfile:
            #Storing the given data in json format in same folder
            json.dump(response_data, outfile, indent=4)    


