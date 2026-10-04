class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
        return slow
# For testing locally
nums = [1, 1, 2, 2, 3]
s = Solution()
k = s.removeElement(nums,1)
print(k)
print(nums[:k])