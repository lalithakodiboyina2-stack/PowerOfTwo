class Solution:
    def isPowerOfTwo(self,n:int) ->bool:
        if n <=0:
            return False
        return(n &(n-1)) == 0
s = Solution()
print(s.isPowerOfTwo(1))
print(s.isPowerOfTwo(16))
print(s.isPowerOfTwo(3))
print(s.isPowerOfTwo(24))

  

    
