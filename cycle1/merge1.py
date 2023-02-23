def mergesort(array):
    if len(array)>1:
        m=len(array)//2
        l = array[:m]
        r = array[m:]

        mergesort(l)
        mergesort(r)
        i = j = k = 0
        while i<len(l) and j<len(r):
            if l[i] < r[j]:
                array[k]=l[i]
                i=i+1
            else:
                array[k]=r[j]
                j=j+1
            k=k+1

        while i < len(l):
            array[k] = l[i]
            i += 1
            k += 1

        while j < len(r):
            array[k] = r[j]
            j += 1
            k += 1

def printlist(array):
    for i in range (len(array)):
        print(array[i],end=" ")
    print()

if __name__ == '__main__':
    arr=[5,2,4,1,7,9,8,3]
    print("the array is: ",end="\n")
    printlist(arr)
    mergesort(arr)
    print("sorted array is:",end = "\n")
    printlist(arr)