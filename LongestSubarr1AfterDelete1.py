class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        mx = 0
        curr = 0
        count = 0
        slow = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                count += 1
            else:
                curr += 1
            if count > 1:
                if nums[slow] == 1:
                    curr -= 1
                if nums[slow] == 0:
                    count -= 1
                slow += 1
            mx = max(mx, curr)

        if mx == len(nums):
            return mx - 1
        return mx