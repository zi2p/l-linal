import math
start = open("input.txt", "r")
final = open("output.txt", "w")

# положение корабля
vx = vy = vz = 0
str1 = list(map(float, start.readline().split()))
vx = str1[0]
vy = str1[1]

# ориентация киля
ax = ay = az = 0
str1 = list(map(float, start.readline().split()))
ax = str1[0]
ay = str1[1]

# направление мачты
mx = my = mz = 1
str1 = list(map(float, start.readline().split()))
mx = str1[0]
my = str1[1]

# положение врага
wx = wy = wz = 0
str1 = list(map(float, start.readline().split()))
wx = str1[0]
wy = str1[1]

start.close()

# угол наклон мачты к вертикали
gamma_cos = 1 / (pow(mx*mx+my*my+mz*mz, 1/2) * 1)
gamma = math.acos(gamma_cos)
gamma = math.degrees(gamma)

# поворот пушки
cx = - vx + wx
cy = - vy + wy
cz = - vz + wz
ninety_betta_cos = abs(cx*ax+ay*cy+az*cz) / (pow(ax*ax+ay*ay+az*az, 1/2) * pow(cx*cx+cy*cy+cz*cz, 1/2))
ninety_betta = math.acos(ninety_betta_cos)
ninety_betta = math.degrees(ninety_betta)
betta = 90 - ninety_betta

# проверка на знак, угол к направлению движения +, против -
if - ((wx - vx) * ax) - ((wy - vy) * ay) >= 0:
    betta = - abs(betta)
    gamma = - abs(gamma)
else:
    betta = abs(betta)
    gamma = abs(gamma)

# вывод
if abs(betta) >= 60:
    print(0, file = final)
elif abs(gamma) >= 60:
    print(0, file = final)
else:
    if ((wx - vx) * ay) - ((wy - vy) * ax) < 0:
        print(1, file = final)
    else:
        print(-1, file = final)
    print(round(betta, 2), file = final)
    print(round(gamma, 2), file = final)
    print("we will win!", file = final)
final.close()
