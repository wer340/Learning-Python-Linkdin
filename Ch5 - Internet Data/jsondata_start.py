# 
# Example file for parsing and processing JSON
# LinkedIn Learning Python course by Joe Marini
#
from datetime import date
import json
import urllib.request 

def printResults(data):
    # Use the json module to load the string data into a dictionary
    theJSON = json.loads(data)
    # this line  json data parse  for easy handle 
    # now we can access the contents of the JSON like any other Python object
    
    if "title" in  theJSON["metadata"]:
        print("title of API : ", theJSON["metadata"]["title"])
   
    # output the number of events, plus the magnitude and each event name  
    if "count" in theJSON["metadata"]:
        print(theJSON["metadata"]["count"],"count of  earthquake in record")
    
    for i in theJSON["features"]:
        print("magnitude of earthquake : " , i["properties"]["mag"]) 
    # for each event, print the place where it occurred
    for i in theJSON["features"]:
        
        print("%2.1f **"%i["properties"]["mag"],i["properties"]["place"]) #%4.7f  means  4 digit  integer an 7 digit decimal
        text=str(i["properties"]["mag"])+i["properties"]["place"]
        with open('./list.txt',"a+",encoding="utf8") as file:
            file.write(text+"\n")
    with open('./list.txt',"a+",encoding="utf8") as file:
        file.write("**************************************************************\n")
    # print the events that only have a magnitude greater than 4
    for i in theJSON["features"]:
        if i["properties"]["mag"]>4.0:
            print("earthquake greater than 4 " , "%2.1f **"%i["properties"]["mag"],i["properties"]["place"])

    # print only the events where at least 1 person reported feeling something
    for i in theJSON["features"]:
         if i["properties"]["felt"]!=None:
            if i["properties"]["felt"]>0:
                print("felt time   : ",i["properties"]["felt"] , "### %2.1f **"%i["properties"]["mag"],i["properties"]["place"])
  
def main():
    # define a variable to hold the source URL
    # In this case we'll use the free data feed from the USGS
    # This feed lists all earthquakes for the last day larger than Mag 2.5
    urlData = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"
    # Open the URL and read the data
    webUrl = urllib.request.urlopen(urlData)
    print ("result code: " + str(webUrl.getcode()))
    # try :
    data_e=webUrl.read()
    # print(data_e)
    printResults(data_e)
    # except:
    #     print("error ocurred this error is , " , webUrl.getcode())
if __name__ == "__main__":
    main()
