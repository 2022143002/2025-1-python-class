# 2025.03.18
# 파이썬 리스트 : 한개의 변수의 여러 값을 할당

#인덱싱
colors = ['red', 'blue', 'green']
print(colors) # list 전체 출력
print(colors[1]) # list 두번째 원소 출력, 0부터 시작
print(colors[-1]) # 리스트 마지막 원소 출력
print(len(colors)) # 리스트 같이 출력

# 슬라이싱
cities = ['서울', '부산', '인천', '의정부', '대전', '강릉', '논산', '포항']
print(cities[0:5]) # cities[0:n] 0~n-1까지 표시
print(cities[:7]) # 0~6번째 원소
print(cities[:-1]) # 0~-2까지
print(cities[3:])
print(cities[:]) # 전부 표시
print(cities[-4:]) # 뒤에서 4번째부터 표시
print(cities[:7:2]) # 처음부터 6번째 원소까지, 한 칸씩 건너뜀
print(cities[::3]) # 처음부터 끝까지, 세 칸씩 건너뜀
print(cities[::-1]) # 처음부터 끝까지, 거꾸로
print(cities[4::-2])

# 리스트의 추가
colors = ['red', 'blue', 'green']
colors.append('white')
print(colors[:])
colors.extend(['balck', 'purple'])
print(colors[:])
colors.insert(1, 'orenge')
print(colors[:])
colors.remove('purple')
print(colors[:])
colors[1] = 'sky'
print(colors[:])

# 패킹, 언패킹
c1, _, c2, c3, _, _ = colors
print(c1, c2, c3)

first = ['egg', 'salad', 'bread', 'soup', 'canafe']
second = ['fish', 'lamb', 'pork', 'beef', 'chicken']
third = ['apple', 'banana', 'orange', 'grape', 'mango']

order = [first, second, third]
john = [order[0][:-2], second[1::3], third[0]]
del john[2]
john.extend([order[2][0:1]])
print(john)