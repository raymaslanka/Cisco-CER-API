import hashlib
import requests
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup

ip_add = input("\nPlease enter CER Server IP address: ")
cer_version = input("Please enter major CER version, i.e. 10, 11, 12: ")
username = input("Please enter CER username: ")
password = input("Please enter CER user password: ")

if cer_version != "10":
   # decrypt password to sha256
   sha_password = hashlib.sha256(password.encode()).hexdigest()
   # create authentication URL
   print("\nAuthenticating...")
   resp = requests.get('http://' + ip_add + '/cerappservices/export/authenticate/status/' + username + "/" + sha_password)
   soup = BeautifulSoup(resp.text, "xml")
   # print(soup.prettify())
   print("Status:",soup.status.string)
else:
   # need to test this somewhere
   # I don't have access 
   resp = requests.get('http://' + ip_add + '/cerappservices/export/authenticate/status/' + username + "/" + password)
   soup = BeautifulSoup(resp.text, "xml")
   # print(soup.prettify())
   print("Status:",soup.status.string)

print("\nGet Licensing Info...")
resp = requests.get('http://' + ip_add + '/cerappservices/export/e911licensemanager/info/' + username + "/" + sha_password)
soup = BeautifulSoup(resp.text, "xml")
# print(soup.prettify())
print("CER License Status:",soup.AuthorizationStatus.string)
print("CER Phones Discovered:",soup.NoPhonesDiscovered.string)
