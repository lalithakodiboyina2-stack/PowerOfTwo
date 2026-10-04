def isPalindrome(n):
    if n <0:
        return False
    temp = n
    rev = 0
    while temp > 0:
        rev = rev * 10 + temp % 10
        temp //= 10
    return rev == n
print(isPalindrome(121))
print(isPalindrome(123))
print(isPalindrome(1221))