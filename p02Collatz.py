# 2025.04.02 파일썬 수업 프로젝트 두 번째
# 콜라츠 추측, 또는 우박수
# 1부터 1000까지의 숫자 중, 가장 많은 단계를 거쳐서 1호 가는 수는 무엇인가?, 가장 많은 단계는 몇 단계인가
# 규칙: n이 짝수 -> n/2
#      n이 홀수 -> 3 * n + 1
#  예: 5 -> 16 -> 8 -> 4 -> 2 -> 1  (5단계)
from numpy.ma.core import max_val
from tornado.httputil import parse_response_start_line

n = 9
# 단계의 갯수를 셀 것 - done
# n을 99부터 1까지 변화하면서, 각각의 단계수를 출력할 것
# 그 중 가장 큰 수를 찾을 것
# n=97: 118번 만에 1호 도달

maxvalue = 0
max1 = 0
max2 = 0

for n in range(1,100):
    print(f'{n=}')
    ncount = 0
    i = n

    while i != 1:
        if i % 2 == 1:
            i = 3 * i + 1
        else:
            i = i / 2
        ncount = ncount + 1

    print(f'{ncount}')
    if maxvalue < ncount:
        maxvalue = ncount
        max1 = n

print(f'{maxvalue=}, {max1=}')


# for i in range(1,100):
#     while n != 1:
#         if n % 2 == 1:
#             n = 3 * n + 1
#         else:
#             n = n / 2
#         print(n,i,'단계')

# while n % 2 == 1:
#     if n:
#         n = 3 * n + 1
#     print(n)
# while n % 2 == 0:
#     if n:
#         n = n/2
#     print(n)





