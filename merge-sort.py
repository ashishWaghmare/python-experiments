__author__ = 'ashsihw'

def merge(firstList,secondList):
    if not firstList:
        return secondList
    if not secondList:
        return firstList

    tolalSize=len(firstList)+len(secondList)
    result=[None]*tolalSize
    idxFirst=0
    idxSecond=0
    idxResult=0
    while idxFirst < len(firstList) and idxSecond < len(secondList):
        if firstList[idxFirst] < secondList[idxSecond]:
            result[idxResult]=firstList[idxFirst]
            idxFirst=idxFirst+1
        else:
            result[idxResult]=secondList[idxSecond]
            idxSecond=idxSecond+1
        idxResult=idxResult+1
    while idxFirst < len(firstList):
        result[idxResult]=firstList[idxFirst]
        idxResult=idxResult+1
        idxFirst=idxFirst+1
    while idxSecond < len(secondList):
        result[idxResult]=secondList[idxSecond]
        idxResult=idxResult+1
        idxSecond=idxSecond+1
    return result

def msort(list):
    length=len(list)
    if length <= 1:
        return list
    half=length//2
    firstHalf=list[:half]
    secondHalf=list[half:]
    firstHalf=msort(firstHalf)
    secondHalf=msort(secondHalf)
    return  merge(firstHalf,secondHalf)


val=[1,2,4,3,14,6,7,9,8]
val=msort(val)
print(val)
