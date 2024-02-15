def pad(input):
    encodedInput = [char.encode('utf-8') for char in input]

    padding = 16 - (len(encodedInput) % 16)
    encodedInput += [padding.to_bytes(1, 'big')] * padding

    return b''.join(encodedInput)

def unpad(input):
    # encodedInput = [char.encode('utf-8') for char in input]
    encodedInput = input
    
    # padding = int.from_bytes(encodedInput[-1], 'big')
    padding = encodedInput[-1]

    tempPadding = encodedInput[len(encodedInput) - padding:]

    for pad in tempPadding:
        if pad != padding:
            raise Exception("invalid padding")

    unpaddedInput = encodedInput[0:len(encodedInput) - len(tempPadding)]
    
    return str(unpaddedInput, encoding='utf-8')

