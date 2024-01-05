class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        point = 0

        for mover in range(len(nums)):
            if nums[mover] != 0:
                nums[mover], nums[point] = nums[point], nums[mover]
                point += 1
        return nums
    
if __name__ == '__main__':
    nums = [0,1,0,3,12]
    solution = Solution()
    print(solution.moveZeroes(nums))

# Two pointers

# 1, 0, 0, 3, 12
# 1, 0, 0, 3, 12
# 1, 3, 0, 0, 12
# 1, 3, 0, 0, 12
# 1, 3, 12, 0, 0
    