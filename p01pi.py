# 오일러 공식을 이용한 파이 근사 값 구하기

p = 1

n = 1
p = p * ((2 * n + 1)**2 - 1)/(2 * n + 1)**2

n = 2
p = p * ((2 * n + 1)**2 - 1)/(2 * n + 1)**2
print(p*4)


i = 1
for j in range(1,100):
    i = i * ((2 * j + 1) ** 2 - 1) / (2 * j + 1) ** 2
    print(i*4)

# 루프로 변환

i = 1
pilist = []
for j in range(1,1000):
    i = i * ((2 * j + 1) ** 2 - 1) / (2 * j + 1) ** 2
    # print(i*4, ',')
    pilist.append(i*4)

import matplotlib.pyplot as plt
plt.plot(pilist)
plt.show()




