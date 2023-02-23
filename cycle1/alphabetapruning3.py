Max, Min = 1000, -1000
def minmax(depth,nodeindex,maximizingplayer,values,alpha,beta):
    if depth==3:
        return values[nodeindex]
    if maximizingplayer:
        best = Min
        for i in range(0,2):
            eva = minmax(depth+1, nodeindex * 2 +i, False,values,alpha,beta)
            best = max(best,eva)
            alpha  = max(alpha,best)
            if beta<=alpha:
                break
        return best
    else:
        best = Max
        for i in range(0,2):
            eva = minmax(depth+1, nodeindex * 2 + i, True,values,alpha, beta)
            best = min(best,eva)
            beta = min(beta,best)

            if beta<=alpha:
                break
        return best

values=[3, 5, 6, 9, 1, 2, 0, -1]
print("The optimal value is :", minmax(0, 0, True, values, Min, Max))