import requests

homeURL = 'http://localhost:8080'
regesterURL = 'http://localhost:8080/register'

# WHY WAS IT 32 BYTES?

session = requests.Session()
userAdmin = "xxxxxxxxxxxadmin"
# print(len(userAdmin))
userAdmin = [*userAdmin]
userAdmin += '\x00' * (10) + '\x0b'
# print(userAdmin)
# userAdminStr = ""
# for i in userAdmin:
#     userAdminStr += i
userAdmin = "".join(userAdmin)
# print(len(userAdmin))

# get rid of the last block (16 bytes)
uidAtBlockEnd = {"user" : "xxxxxxxxxxxxxxx", "password" : "password"}

# only take the second block and put that at the end of the previous cookie
registerPayloadAdmin = {"user" : userAdmin, "password" : "password"}

# for cookie one
session.post(regesterURL, data=uidAtBlockEnd)
session.post(homeURL, data=uidAtBlockEnd)

requests.get('http://localhost:8080/home')
cookieOne = session.cookies.get_dict().get('auth_token')
# print(cookieOne)
cookieOne = cookieOne[: (len(cookieOne) -32 )]
# print(cookieOne)

# for cookie two
session.post(regesterURL, data=registerPayloadAdmin)
session.post(homeURL, data=registerPayloadAdmin)

requests.get('http://localhost:8080/home')
cookieTwo = session.cookies.get_dict().get('auth_token')
# print(cookieTwo)
cookieTwo = cookieTwo[32:64]
# print(cookieTwo)


cookie = cookieOne + cookieTwo
print(cookie)

session.cookies.set('auth_token', cookie)
result = session.get('http://localhost:8080/home')
print(result.text)

# one of the blocks where role equals is at the end of a block
# one cookie where the username is admin
# http request to get admin as 
# padding admin padding
# or find a user with valid padding bytes 