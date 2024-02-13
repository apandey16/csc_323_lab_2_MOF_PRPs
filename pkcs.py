def pad(input):
    encodedInput = [char.encode('utf-8') for char in input]

    padding = 16 - (len(encodedInput) % 16)
    encodedInput += [padding.to_bytes(1, 'big')] * padding

    return encodedInput

def unpad(input):
    encodedInput = [char.encode('utf-8') for char in input]
    
    padding = int.from_bytes(encodedInput[-1], 'big')

    tempPadding = encodedInput[len(encodedInput) - padding:]

    for pad in tempPadding:
        if int.from_bytes(pad, 'big') != padding:
            raise Exception("invalid padding")
    
    unpaddedInput = encodedInput[:padding]
    
    return unpaddedInput

