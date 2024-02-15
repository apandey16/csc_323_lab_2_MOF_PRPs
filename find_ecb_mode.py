import operator
from encodeAndDecode import convertToBytes, convertToHex;

def decodeLines(lines):
    retLst = []
    for line in lines:
        retLst.append(convertToBytes(line)[54:])
    return retLst

# if there is a pattern within the decrypted value, it is ECB b/c each part of the CT is encrypted seperatly so there will be repetition
def find_ecb_mode(lines):
    offset = 0
    retLine = None
    retLineIdx = None

    for line in lines:
        curChunck = line[offset: offset+16]
        
        windows = []
        for i in range(0, len(line), 16):
            windows.append(line[i: i + 16])
        

        segmentDict ={}

        segmentDict[curChunck] = 0

        for window in windows:
            if curChunck == window:
                segmentDict[window] += 1
            else:
                segmentDict[window] = 1
        segmentLst = sorted(segmentDict.items(), key=operator.itemgetter(1), reverse=True)
        # print((segmentLst[0][1]))
        if segmentLst[0][1] > 1:
            retLine = line
            retLineIdx = lines.index(line)
        offset += 16
    
    return retLine, retLineIdx

def main():
    f = open("testDocs/Lab2.TaskII.B.txt")
    flines = f.read().splitlines()
    f.close()
    
    ecbLine, ecbLineIdx = find_ecb_mode(decodeLines(flines))
    
    ecbLine = convertToBytes(flines[ecbLineIdx])

    fw = open("image.bmp", "wb")
    fw.write(ecbLine)
    fw.close()

if __name__ == "__main__":
    main()