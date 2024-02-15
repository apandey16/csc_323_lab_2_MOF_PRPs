import binascii
from encodeAndDecode import base64Decode;
from pkcs import pad, unpad;
from Crypto.Cipher import AES;

def ecb_encrypt(key, plaintext):
    paddedPT = pad(plaintext)
    print(paddedPT)

    cipher = AES.new(key, AES.MODE_ECB)

    cipherText = cipher.encrypt(paddedPT)

    # print(binascii.hexlify(cipherText))
    return cipherText

def ecb_decrypt(key, ciphertext):
    if len(ciphertext) % 16 != 0:
        raise Exception("CT error")
    # print("CT")
    # print(ciphertext)

    decipher = AES.new(key, AES.MODE_ECB)

    decipheredText = decipher.decrypt(ciphertext)

    plainText = unpad(decipheredText)

    return plainText


# print(ecb_decrypt(b'Sixteen byte key', ecb_encrypt(b'Sixteen byte key', "testtestetstetstetstetstetstets")))

def main ():
    f = open("testDocs/Lab2.TaskII.A.txt")
    flines = f.read().rstrip()
    f.close()
    # print(len(flines))

    decodeLine = base64Decode(flines)
    # print(len(decodeLine))
    try:
        print(ecb_decrypt(b'CALIFORNIA LOVE!', decodeLine))
    except Exception as e:
        print(e)

        

if __name__ == "__main__":
    main()