result = 0
i = 0
while i < 1000:
    if i % 3 == 0:
        result +=i
    elif i % 5 ==0:
        result +=i
    elif i%3==0 & i%5==0:
        result -=i
    i+=1
print(result)