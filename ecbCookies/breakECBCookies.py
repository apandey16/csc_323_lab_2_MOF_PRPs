import requests
import re

homeURL = 'http://localhost:8080'
regesterURL = 'http://localhost:8080/register'

session = requests.Session()
userAdmin = "xxxxxxxxxxxadmin"
userAdmin = [*userAdmin]
userAdmin += '\x00' * (11 - 1) + chr(11)
userAdmin = "".join(userAdmin)

# get rid of the last block (16 bytes)
uidAtBlockEnd = {"user" : "xxxxxxxxxxxxxxx", "password" : "password"}
# only take the second block and put that at the end of the previous cookie
registerPayloadAdmin = {"user" : userAdmin, "password" : "password"}

# for cookie one
session.post(regesterURL, data=uidAtBlockEnd)
session.post(homeURL, data=uidAtBlockEnd)

requests.get('http://localhost:8080/home')
cookieOne = session.cookies.get_dict().get('auth_token')
cookieOne = cookieOne[: (len(cookieOne) -16 )]
print(cookieOne)

# for cookie two
session.post(regesterURL, data=registerPayloadAdmin)
session.post(homeURL, data=registerPayloadAdmin)
requests.get('http://localhost:8080/home')
cookieTwo = session.cookies.get_dict().get('auth_token')
cookieTwo = cookieTwo[16:32]
print(cookieTwo)


cookie = cookieOne + cookieTwo
print(cookie)

#one of the blocks where role equals is at the end of a block
# one cookie where the username is admin
#http request to get admin as 
# padding admin padding
# or find a user with valid padding bytes 
# role = admin ; user = admin