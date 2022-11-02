import urllib.parse
import requests
main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "oOlYYEjw32FoGgJH32jSDjzCC9CgjUGD"
while True:
    orig = input("Starting Location: ")
    if orig == "quit" or orig == "q":
        break
    dest = input("Destination: ")
    if dest == "quit" or dest == "q":
        break
    url = main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest})
    print("URL: " + (url))
    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]
    if json_status == 0:
       print("API Status: " + str(json_status) + " = A successful route call.\n")
       print("=============================================")
       print("In exact " 
       + (json_data["route"]["formattedTime"] 
       + " Minutes " 
       + " With a Kilometers of : " + str("{:.2f}".format((json_data["route"]["distance"])*1.61) 
       + " You will reach the destination from " + (orig) + " to " + (dest))))
       
       print("Realtime: " + str(json_data["route"]["realTime"]))
       print("Vehicle Type: " + str(json_data["route"]["legs"][0]["maneuvers"][0]["transportMode"]))
       print("")

       print("Directions Guide:")
       
       for each in json_data["route"]["legs"][0]["maneuvers"]:
            print((each["narrative"]) + " (" + str("{:.2f}".format((each["distance"])*1.61) + " km)"))
    elif json_status == 402:
     print("Status Code: " + str(json_status) + " = Invalid user input for one or both locations.")
    elif json_status == 611:
     print("Status Code: " + str(json_status) + " = Missing an entry for one or both locations.")
    else:
     print("For Staus Code: " + str(json_status) + "; Refer to:")
     print("https://developer.mapquest.com/documentation/directions-api/status-codes")
     print("************************************************************************\n")
