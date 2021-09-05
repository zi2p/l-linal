start = open("input.txt", "r")
final = open("output.txt", "w")
GOOD = 1
A = []
B = []
C = []
D = []
F = []
                  # матрицы
a = 0
b = 0                                      # константы
na = ma = nb = mb = nc = mc = nf = mf = 0        # параметры матриц

str1 = list(map(float, start.readline().split()))

a = str1[0]
b = str1[1]

str2 = list(map(int, start.readline().split()))
na = str2[0]
ma = str2[1]
str3 = list(map(float, start.readline().split()))
for i in range(na):                                            # матрица А
    AM = []
    for j in range(ma):
        AM.append(str3[i*ma+j])
    A.append(AM)

str4 = list(map(int, start.readline().split()))
nb = str4[0]
mb = str4[1]
str5 = list(map(float, start.readline().split()))
for i in range(nb):
    BM = []                                                     # матрица В
    for j in range(mb):
        BM.append(str5[i * mb + j])
    B.append(BM)

str6 = list(map(int, start.readline().split()))
nc = str6[0]
mc = str6[1]

str7 = list(map(float, start.readline().split()))

for i in range(nc):
    CM = []                                                     # матрица C
    for j in range(mc):
        CM.append(str7[i * mc + j])
    C.append(CM)

str8 = list(map(int, start.readline().split()))
nd = str8[0]
md = str8[1]
str9 = list(map(float, start.readline().split()))

for i in range(nd):
    DM = []                                                     # матрица D
    for j in range(md):
        DM.append(str9[i * md + j])
    D.append(DM)

str10 = list(map(int, start.readline().split()))
nf = str10[0]
mf = str10[1]
str11 = list(map(float, start.readline().split()))
for i in range(nf):
    FM = []                                                     # матрица F
    for j in range(mf):
        FM.append(str11[i * mf + j])
    F.append(FM)

# умножаем А на константу а

for i in range(na):                                            # матрица a*А
    for j in range(ma):
        A[i][j] *= a

# транспанируем В

transp0 = []
if (GOOD != 0):
    for i in range(mb):
        list0 = []
        for j in range(nb):
            list0.append(0)
        transp0.append(list0)
    for i in range(mb):
        for j in range(nb):
            transp0[i][j] = B[j][i]
change = mb
mb = nb
nb = change
# транспанированную умножаем на константу
if GOOD != 0:
    for i in range(nb):                                            # матрица b*Bt
        for j in range(mb):
            transp0[i][j] *= b
# складываем переменоженное

if GOOD != 0:
    if (nb != na) or (ma != mb):
        GOOD = 0
    if (nb == na) and (ma == mb):
        summa = []
        for i in range(na):
            list1 = []
            for j in range(ma):
                list1.append(0)
            summa.append(list1)
        for i in range(na):
            for j in range(ma):
                summa[i][j] = A[i][j] + transp0[i][j]

#  транспанируем сумму

transp1 = []
if (GOOD != 0):
    for i in range(mb):
        list2 = []
        for j in range(nb):
            list2.append(0)
        transp1.append(list2)
    for i in range(mb):
        for j in range(nb):
            transp1[i][j] = summa[j][i]
else:
    GOOD = 0

# умножаем С на транспонированную

change = mb
mb = nb
nb = change
if (mc == nb) and (GOOD != 0):
    CX = []
    for i in range(nc):
        list3 = []
        for j in range(mb):
            list3.append(0)
        CX.append(list3)
    for i in range(nc):
        for j in range(mb):
            for k in range(mc):
                CX[i][j] += C[i][k] * transp1[k][j]
else:
    GOOD = 0
# полученное умножаем на D

nCX = nc
mCX = mb

if (mCX == nd) and (GOOD != 0):
    XD = []
    for i in range(nCX):
        list4 = []
        for j in range(md):
            list4.append(0)
        XD.append(list4)
    for i in range(nCX):
        for j in range(md):
            for k in range(mCX):
                XD[i][j] += CX[i][k] * D[k][j]
else:
    GOOD = 0
# полученное -F
nXD = nCX
mXD = md

if (nf == nXD) and (mf == mXD) and (GOOD != 0):
    not_summa = []
    for i in range(nXD):
        list5 = []
        for j in range(mXD):
            list5.append(0)
        not_summa.append(list5)

    for i in range(nXD):
        for j in range(mXD):
            not_summa[i][j] = XD[i][j] - F[i][j]
else:
    GOOD = 0
if GOOD == 0:
    print(0, file = final)
else:
    print(1, file = final)
    print(len(not_summa), len(not_summa[0]), file = final)
    for i in range(len(not_summa)):
        for j in range(len(not_summa[0])):
            print(not_summa[i][j], end = ' ', file = final)

final.close()
start.close()
