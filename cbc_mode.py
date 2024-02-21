from Crypto.Cipher import AES
from pkcs import pad, unpad
from encodeAndDecode import base64Decode, base64Encode;

def cbc_encrypt(plaintext, key, iv):
    paddedPT = pad(plaintext)
    print(paddedPT)

    cipher = AES.new(key, AES.MODE_CBC, iv)

    cipherText = cipher.encrypt(paddedPT)

    return cipherText

def cbc_decrypt(ciphertext, key, iv):
    if len(ciphertext) % 16 != 0:
        raise Exception("CT error")

    decipher = AES.new(key, AES.MODE_CBC, iv)

    decipheredText = decipher.decrypt(ciphertext)

    plainText = unpad(decipheredText)

    return plainText

def main ():
    f = open("testDocs/Lab2.TaskIII.A.txt")
    flines = f.read().rstrip()
    f.close()

    decodeLine = base64Decode(flines)
    
    print(cbc_decrypt(decodeLine[16:], b'MIND ON MY MONEY',decodeLine[:16]))
        

if __name__ == "__main__":
    main()