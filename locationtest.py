import requests
    
WEBSERVICES_BASE = "http://51.143.186.87:8080"
personid = "{12345-test-person-id}"
location = "testlocation"

url = WEBSERVICES_BASE + "/appearance/" + personid
body = location
requests.put(url,data=body)