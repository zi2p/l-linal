def ore_partum(ax, ay, az, bx, by, bz, cx, cy, cz, ind):
    global ore_A, ore_B, ore_C, ore_D
    ore_A[ind] = ((by - ay) * (cz - az)) - ((cy - ay) * (bz - az))
    ore_B[ind] = ((cx - ax) * (bz - az)) - ((bx - ax) * (cz - az))
    ore_C[ind] = ((bx - ax) * (cy - ay)) - ((by - ay) * (cx - ax))
    ore_D[ind] = -(ax*(by-ay)*(cz-az)-ax*(cy-ay)*(bz-az))-(ay*(bz-az)*(cx-ax)-ay*(bx-ax)*(cz-az))-(az*(bx-ax)*(cy-ay)-az*(by-ay)*(cx-ax))
    print(ore_A[ind],ore_B[ind],ore_C[ind],ore_D[ind])

def intersectio(ind, A, B, C, D):
    # пересекаются, если скалярное произведением направляющего вектора луча и нормали плоскости не ноль
    rezult = A[ind] * trabes_vector_x + B[ind] * trabes_vector_y + C[ind] * trabes_vector_z
    if rezult != 0:
        lambd = -(D[ind] + A[ind] * input_trabes_x + B[ind] * input_trabes_y + C[ind] * input_trabes_z) / rezult
        if lambd <= 0:  # не в сторону направления луча
            return 0
        if lambd > 0:
            return lambd
    else:
        return 0

def coefficiens(i):
    A = -planum_x[i]
    B = -planum_y[i]
    C = -planum_z[i]
    k = -2 * (trabes_vector_x * A + trabes_vector_y * B + trabes_vector_z * C) / ( A**2 + B**2 + C**2)
    return k

def reflexionem_a_speculo(ind):
    # преобразуем ход луча
    global trabes_vector_x, trabes_vector_y, trabes_vector_z, E0
    lambd = coefficiens(ind)
    trabes_vector_x = trabes_vector_x - (lambd * planum_x[ind])
    trabes_vector_y = trabes_vector_y - (lambd * planum_y[ind])
    trabes_vector_z = trabes_vector_z - (lambd * planum_z[ind])
    E0 -= 1
    if E0 == 0:
        print(E0, file=finish)
        print(input_trabes_x, input_trabes_y, input_trabes_z, file=finish)
        finish.close()

def puncto_reflexio(lambd):
    # точка отражения, теперь от нее отсчитывается направление луча
    global input_trabes_x, input_trabes_y, input_trabes_z
    global trabes_vector_x, trabes_vector_y, trabes_vector_z
    input_trabes_x = lambd * trabes_vector_x + input_trabes_x
    input_trabes_y = lambd * trabes_vector_y + input_trabes_y
    input_trabes_z = lambd * trabes_vector_z + input_trabes_z

def punctum_fuga(ind):
    # точка улёта
    global input_trabes_x, input_trabes_y, input_trabes_z, fly
    global trabes_vector_x, trabes_vector_y, trabes_vector_z
    lambd = -(ore_D[ind] + ore_A[ind] * input_trabes_x + ore_B[ind] * input_trabes_y + ore_C[ind] * input_trabes_z) / (ore_A[ind] * trabes_vector_x + ore_B[ind] * trabes_vector_y + ore_C[ind] * trabes_vector_z)
    input_trabes_x = lambd * trabes_vector_x + input_trabes_x
    input_trabes_y = lambd * trabes_vector_y + input_trabes_y
    input_trabes_z = lambd * trabes_vector_z + input_trabes_z
    print(fly, file=finish)
    print(E0, file=finish)
    print(input_trabes_x, input_trabes_y, input_trabes_z, file=finish)
    print(trabes_vector_x, trabes_vector_y, trabes_vector_z, file=finish)
    finish.close()

start = open("input.txt", "r")
finish = open("output.txt", "w")
# читаем координаты вершин куба
str1 = list(map(float, start.readline().split()))
Ax = str1[0]
Ay = str1[1]
Az = str1[2]

str1 = list(map(float, start.readline().split()))
Bx = str1[0]
By = str1[1]
Bz = str1[2]

str1 = list(map(float, start.readline().split()))
Cx = str1[0]
Cy = str1[1]
Cz = str1[2]

# для удобства под С1 считаю D
str1 = list(map(float, start.readline().split()))
C1x = str1[0]
C1y = str1[1]
C1z = str1[2]

# найдем координаты остальных вершин
Dx = (Ax - Bx) + (Cx - Bx) + Bx
Dy = (Ay - By) + (Cy - By) + By
Dz = (Az - Bz) + (Cz - Bz) + Bz

B1x = (Bx - Cx) + (C1x - Cx) + Cx
B1y = (By - Cy) + (C1y - Cy) + Cy
B1z = (Bz - Cz) + (C1z - Cz) + Cz

A1x = (Ax - Bx) + (B1x - Bx) + Bx
A1y = (Ay - By) + (B1y - By) + By
A1z = (Az - Bz) + (B1z - Bz) + Bz

D1x = (A1x - B1x) + (C1x - B1x) + B1x
D1y = (A1y - B1y) + (C1y - B1y) + B1y
D1z = (A1z - B1z) + (C1z - B1z) + B1z

# считывание направляющего вектора входящего луча
str1 = list(map(float, start.readline().split()))
trabes_vector_x = str1[0]
trabes_vector_y = str1[1]
trabes_vector_z = str1[2]

# координаты точки входа
str1 = list(map(float, start.readline().split()))
input_trabes_x = str1[0]
input_trabes_y = str1[1]
input_trabes_z = str1[2]

str1 = list(map(int, start.readline().split()))
E0 = str1[0]

str1 = list(map(int, start.readline().split()))
N = str1[0]

# считывание точек плоскости зеркал
glass_x1 = [0] * N
glass_y1 = [0] * N
glass_z1 = [0] * N

glass_x2 = [0] * N
glass_y2 = [0] * N
glass_z2 = [0] * N

glass_x3 = [0] * N
glass_y3 = [0] * N
glass_z3 = [0] * N

for index in range(0, N):
    srt1 = list(map(float, start.readline().split()))
    glass_x1[index] = srt1[0]
    glass_y1[index] = srt1[1]
    glass_z1[index] = srt1[2]
    srt1 = list(map(float, start.readline().split()))
    glass_x2[index] = srt1[0]
    glass_y2[index] = srt1[1]
    glass_z2[index] = srt1[2]
    srt1 = list(map(float, start.readline().split()))
    glass_x3[index] = srt1[0]
    glass_y3[index] = srt1[1]
    glass_z3[index] = srt1[2]

# создание уравнения плоскости зеркал
planum_x = [0] * N
planum_y = [0] * N
planum_z = [0] * N
planum_D = [0] * N

for i in range(0, N):
    planum_x[i] = ((glass_y2[i] - glass_y1[i]) * (glass_z3[i] - glass_z1[i])) - ((glass_y3[i] - glass_y1[i]) * (glass_z2[i] - glass_z1[i]))
    planum_y[i] = ((glass_x3[i] - glass_x1[i]) * (glass_z2[i] - glass_z1[i])) - ((glass_x2[i] - glass_x1[i]) * (glass_z3[i] - glass_z1[i]))
    planum_z[i] = ((glass_x2[i] - glass_x1[i]) * (glass_y3[i] - glass_y1[i])) - ((glass_x3[i] - glass_x1[i]) * (glass_y2[i] - glass_y1[i]))
    planum_D[i] = -((planum_x[i] * glass_x1[i]) + (planum_y[i] * glass_y1[i]) + (planum_z[i] * glass_z1[i]))

# создаем уравнения граней
ore_A = [0] * 6
ore_B = [0] * 6
ore_C = [0] * 6
ore_D = [0] * 6

ore_partum(Ax, Ay, Az, Bx, By, Bz, Cx, Cy, Cz, 0)
ore_partum(A1x, A1y, A1z, B1x, B1y, B1z, C1x, C1y, C1z, 1)
ore_partum(Ax, Ay, Az, Bx, By, Bz, B1x, B1y, B1z, 2)
ore_partum(B1x, B1y, B1z, Bx, By, Bz, Cx, Cy, Cz, 3)
ore_partum(C1x, C1y, C1z, Dx, Dy, Dz, Cx, Cy, Cz, 4)
ore_partum(Ax, Ay, Az, Dx, Dy, Dz, A1x, A1y, A1z, 5)

fly = 0
while (E0 > 0) & (fly == 0):       # пока есть энергия и не вылетел
    minimum = float("inf")
    for i in range(0, N):
        lambd_mir = intersectio(i, planum_x, planum_y, planum_z, planum_D)
        if (lambd_mir < minimum) & (lambd_mir > 0):
            minimum = lambd_mir
            intersectio_planum = i                                                        # запоминаем номер зеркала
    for i in range(0, 6):
        lambd_place = intersectio(i, ore_A, ore_B, ore_C, ore_D)
        if (lambd_place < minimum) & (lambd_place > 0):
            minimum = lambd_place
            intersectio_ore = i                                                              # запоминаем номер грани
            fly = 1
    if fly:                                                # улетел
        punctum_fuga(intersectio_ore)
    else:                                                 # не улетел
        puncto_reflexio(minimum)                         # новая точка(отражение)
        reflexionem_a_speculo(intersectio_planum)       # преобразование луча
start.close()
