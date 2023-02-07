def create_matrix(row,col,datalist):
    mat=[]
    for i in range(row):
        rowlist=[]
        for j in range(col):
            rowlist.append(datalist[row*i+j])
        mat.append(rowlist)
    return mat
def main():
    df=['a','b','c','d','e','f','g','h','i']
    mat=create_matrix(3,3,df)
    print(mat)

main()