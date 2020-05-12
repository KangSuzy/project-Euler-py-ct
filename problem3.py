# 가장 큰 소인수 구하기
x = 600851475143
max_prime = 0
i = 2

while x != 1:
    while x % i == 0:
        max_prime = i
        x = x // i
    i += 1
print(max_prime)