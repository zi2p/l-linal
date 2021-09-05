def determinant(A1,B1,C1,A2,B2,C2,A3,B3,C3):
    r = A1*B2*C3 + A2*B3*C1 + B1*C2*A3 - A3*B2*C1 - C2*B3*A1 - B1*A2*C3
    return r

def wr1(i1,i2,ip):
    global ssss
    for i in range(ko):
        if i>ip:
            if p[i]!=-1:
                if p[i][0]*n1[i1]+p[i][1]*n2[i1]+p[i][2]*n3[i1]+D[i1]==0 and p[i][0]*n1[i2]+p[i][1]*n2[i2]+p[i][2]*n3[i2]+D[i2]==0:
                    ssss+=1
                    return

def wr(i1,i2,ip):
    for i in range(ko):
        if i>ip:
            if p[i]!=-1:
                if p[i][0]*n1[i1]+p[i][1]*n2[i1]+p[i][2]*n3[i1]+D[i1]==0 and p[i][0]*n1[i2]+p[i][1]*n2[i2]+p[i][2]*n3[i2]+D[i2]==0:
                    print(p[i][0],p[i][1],p[i][2], p[ip][0],p[ip][1],p[ip][2], file=final)
                    return

start = open("input.txt", "r")
final = open("output.txt", "w")
str1 = list(map(int, start.readline().split()))
M = str1[0]   # число задаваемых плоскостей
n1 = [0] * M            # векторы нормали (наружу многогранника)
n2 = [0] * M
n3 = [0] * M
r1 = [0] * M             # радиус-векторы точкек плоскостей
r2 = [0] * M
r3 = [0] * M
D = [0] * M
for ind in range(0, M):
    str1 = list(map(float, start.readline().split()))
    n1[ind] = str1[0]
    n2[ind] = str1[1]
    n3[ind] = str1[2]
    r1[ind] = str1[3]
    r2[ind] = str1[4]                                                    # создаем уравнения плоскостей
    r3[ind] = str1[5]
    D[ind] = -(n1[ind] * r1[ind] + n2[ind] * r2[ind] + n3[ind] * r3[ind])

if M < 4:                          # невозможно создать многогранник
    print(0, file=final)
    final.close()
    start.close()
else:
    point = [[0] * 3 for i in range(10000)]
    tops = 0
    for i1 in range(0, M - 2):           # запишем вершины (координаты)
        for i2 in range(i1+1, M - 1):
            for i3 in range(i2+1, M):
                if determinant(n1[i1], n2[i1], n3[i1], n1[i2], n2[i2], n3[i2], n1[i3], n2[i3], n3[i3]) != 0:
                    point[tops][0] = abs(-determinant(D[i1], n2[i1], n3[i1], D[i2], n2[i2], n3[i2], D[i3], n2[i3], n3[i3]) / determinant(n1[i1], n2[i1], n3[i1], n1[i2], n2[i2], n3[i2], n1[i3], n2[i3], n3[i3]))
                    point[tops][1] = abs(-determinant(n1[i1], D[i1], n3[i1], n1[i2], D[i2], n3[i2], n1[i3], D[i3], n3[i3]) / determinant(n1[i1], n2[i1], n3[i1], n1[i2], n2[i2], n3[i2], n1[i3], n2[i3], n3[i3]))
                    point[tops][2] = abs(-determinant(n1[i1], n2[i1], D[i1], n1[i2], n2[i2], D[i2], n1[i3], n2[i3], D[i3]) / determinant(n1[i1], n2[i1], n3[i1], n1[i2], n2[i2], n3[i2], n1[i3], n2[i3], n3[i3]))
                    tops += 1    # счёт вершин


    for i1 in range(0, tops-1):
        for i2 in range(i1+1, tops):                # убрать повторения
            if point[i1][0] == point[i2][0] and point[i1][1] == point[i2][1] and point[i1][2] == point[i2][2]:
                point[i1] = [float("inf"), float("inf"), float("inf")]

    cou = 0
    for i1 in range(0, tops):                  # счёт сколько различных точек
        if point[i1][0] != float("inf"):
            cou += 1
    p = [[-1] * 3 for i in range(cou)]
    ko = 0
    for i1 in range(0, tops):
        if point[i1][0] != float("inf"):
            p[ko][0] = point[i1][0]
            p[ko][1] = point[i1][1]
            p[ko][2] = point[i1][2]
            ko += 1
    # если эта точка-вершина, то выполняется следующее:
    ssss = 0
    for i in range(ko):
        for h in range(M):                      # она принадлежит многограннику
            if p[i]!=-1 and p[i][0]!=-1:
                if p[i][0]*n1[h]+p[i][1]*n2[h]+p[i][2]*n3[h]+D[h]>0:
                    p[i]=-1
    s=0

    for i in range(ko):
        if p[i]!=-1 and p[i][0]!=-1:
            s+=1
            for i1 in range(M):
                if p[i][0]*n1[i1]+p[i][1]*n2[i1]+p[i][2]*n3[i1]+D[i1]==0:
                    for i2 in range(M):
                        if p[i][0]*n1[i2]+p[i][1]*n2[i2]+p[i][2]*n3[i2]+D[i2]==0 and i1<i2:
                            wr1(i1,i2,i)

    if ssss < 6 or s < 4:
        print(0, file=final)
        final.close()
        start.close()
    else:
        print(ssss, file=final)
        for i in range(ko):
            for i1 in range(M):
                if p[i]!=-1 and p[i][0]!=-1:
                    if p[i][0]*n1[i1]+p[i][1]*n2[i1]+p[i][2]*n3[i1]+D[i1]==0:
                        for i2 in range(M):
                            if p[i][0]*n1[i2]+p[i][1]*n2[i2]+p[i][2]*n3[i2]+D[i2]==0 and i1<i2:
                                wr(i1,i2,i)
    final.close()
    start.close()
