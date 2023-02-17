string = input("enter the string:")
pattern = input("enter the pattern")

strarr = []
patarr = []
for i in string:
    strarr.append(i)
for j in pattern:
    patarr.append(j)
pindex = 0
sindex = 0
start = sindex
while pindex<len(patarr) and sindex<len(strarr):
    if strarr[sindex]==patarr[pindex]:
        sindex += 1
        pindex += 1
    else:
        sindex = start+1
        start = sindex
        patindex = 0

if pindex==len(patarr):
    print(f"\n pattern is found from the position: \n {start} to {sindex-1-1}")
else:
    print("pattern is not found in the string")