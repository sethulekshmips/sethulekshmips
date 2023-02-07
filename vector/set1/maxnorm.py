
def  max(array):
    max=array[0]
    for i in range (1,len(array)):
        if a[i] > max:
            max=a[i]
    return max

#a=[1,2,3]
#print("largest:",max(a))
def sum(array):
    sum=0
    for i in range(len(array)):
        sum=sum+a[i]
    return sum

a=[1,2,3]
l=max(a)
s=sum(a)
print("maxnorm:",l*s)