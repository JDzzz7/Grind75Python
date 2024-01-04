class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        n = len(nums)

        first = second = float('inf')
        for i in nums:
            if i <= first:
                first = i
            elif i <= second:
                second = i
            else:
                return True
        return False

if __name__ == '__main__':
    nums = [0,4,2,1,0,-1,-3]
    solution = Solution()
    print(solution.increasingTriplet(nums))
