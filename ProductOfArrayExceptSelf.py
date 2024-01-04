class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        product = [1 for i in range(n)]
        prefix = [1 for i in range(n)]
        suffix = [1 for i in range(n)]

        for i in range(1, n):
            prefix[i] = prefix[i-1] * nums[i-1]
        print(prefix)

        for i in range(n-2, -1, -1):
            suffix[i] = suffix[i+1] * nums[i+1]
        print(suffix)

        for i in range(n):
            product[i] = prefix[i] * suffix[i]

        return product
    
if __name__ == '__main__':
    nums = [2, 4, 6, 1, 3, 2]
    solution = Solution()
    print(solution.productExceptSelf(nums))
