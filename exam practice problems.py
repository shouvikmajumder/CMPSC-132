def isprime(n):
    count = 0
    for i in range(1,n+1):
        if n % i == 0:
            count +=1 
    if count>2:
        return False 
    return True

print(isprime(13))

print(isprime(1232))
print(isprime(21))
print(isprime(13))
print(isprime(13))
print(isprime(13))
