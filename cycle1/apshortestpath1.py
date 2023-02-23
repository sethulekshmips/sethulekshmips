v = 4
INF = 999999


def floydwarshall(graph):
    for k in range(v):
        for i in range(v):
            for j in range(v):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
    printsolution(graph)


def printsolution(graph):
    print("The shortest pair path is:")
    print()
    for i in range(v):
        for j in range(v):
            if (graph[i][j] == INF):
                print("%7s" % "inf", end='   ')
            else:
                print("%7d" % graph[i][j], end='   ')
            if j == v - 1:
                print()


graph = [[0, 5, INF, 10],
         [INF, 0, 3, INF],
         [INF, INF, 0, 1],
         [INF, INF, INF, 0]
         ]
floydwarshall(graph)
