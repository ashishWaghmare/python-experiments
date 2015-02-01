__author__ = 'ashsihw'

def sort(list):
    for index in range(len(list)-1,-1,-1):
        for subIndex in range(index,-1,-1):
            print(subIndex,index)
            if(list[subIndex] > list[index]):
                temp=list[subIndex]
                list[subIndex]=list[index]
                list[index]=temp
            print(list)


val=[1,2,4,3]
sort(val)



