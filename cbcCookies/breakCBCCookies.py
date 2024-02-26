import binascii
import requests
import string

homeURL = 'http://localhost:8080'
regesterURL = 'http://localhost:8080/register'

session = requests.Session()
userpadding = "testAuidE1E"
paddingRole = "AroleEadmin" 
junk = "aaaaaaaaaaaaaaaa"

username = userpadding + junk + paddingRole
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
paddingOne = bytearray.fromhex(cookieLst[0])
print(paddingOne)
paddingOne[9] = (paddingOne[9] ^ ord('A')) ^ (ord('&'))
paddingOne[13] = (paddingOne[13] ^ ord('E')) ^ (ord('='))
paddingOne[15] = (paddingOne[15] ^ ord('E')) ^ (ord('&'))
print(paddingOne)
paddingOne = paddingOne.hex()

cookieLst[0] = paddingOne

# need to xor idx 0 and idx 4
paddingTwo = bytearray.fromhex(cookieLst[2])
paddingTwo[0] = (paddingTwo[0] ^ ord('A')) ^ (ord('&'))
paddingTwo[5] = (paddingTwo[5] ^ ord('E')) ^ (ord('='))
paddingTwo = paddingTwo.hex()

cookieLst[2] = paddingTwo

adminCookie = "".join(cookieLst)

print(adminCookie)

session.cookies.set('auth_token', adminCookie)
result = session.get('http://localhost:8080/home')
print(result.text)