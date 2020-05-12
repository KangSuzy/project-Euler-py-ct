# 피보나치 수열에서 400백만 이하이면서 짝수인 항의 합
sum = 0
x = 1
y = 2
while x <= 4000000:
    if x % 2 == 0:
        sum += x
    x, y = y, x + y
print(sum)
