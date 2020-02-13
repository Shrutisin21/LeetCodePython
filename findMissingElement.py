
def findEle(arr1, arr2):
    #return sum(arr1) - sum(arr2)
    arr1 = sorted(arr1)
    arr2 = sorted(arr2)
    for item1, item2 in zip(arr1, arr2):
        if item2 is None:
            return item1
        if item1 != item2:
            return item1



if __name__ == '__main__':
    arr1 = [5,2,3,4,1]
    arr2 = [1,5,4,2]
    print findEle(arr1, arr2)