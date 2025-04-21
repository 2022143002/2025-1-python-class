import numpy as np

def collatz(n):
    steps = 0
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        steps += 1
    return steps

collatz_data = [(i, collatz(i)) for i in range(1, 101)]
sorted_collatz_data = sorted(collatz_data, key=lambda x: x[1], reverse=True)
top_three = sorted_collatz_data[:3]
collatz_list = top_three
collatz_array = np.array(top_three)

print("리스트 형태:", collatz_list)
print("Numpy 배열 형태:\n", collatz_array)