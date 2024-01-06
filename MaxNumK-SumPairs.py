class Solution:
    def maxOperations(self, nums: list[int], k: int) -> int:
        maxOp = 0
        start = 0
        end = len(nums) - 1

        nums.sort()
        
        while start < end:
            sumNum = nums[start] + nums[end]
            if sumNum == k:
                start += 1
                end -= 1
                maxOp += 1
                continue

            if sumNum < k:
                start += 1
            else:
                end -= 1
        return maxOp
    
if __name__ == '__main__':
    nums = [1,2,3,4]
    k = 5
    solution = Solution()
    print(solution.maxOperations(nums, k))