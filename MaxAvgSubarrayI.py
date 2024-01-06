class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        # Sliding Window BB

        currSum = maxSum = sum(nums[:k])

        for i in range(k, len(nums)):
            currSum += nums[i] - nums[i-k]
            maxSum = max(currSum, maxSum)

        maxAvg = maxSum / k
        return maxAvg

if __name__ == '__main__':
    nums = [1,12,-5,-6,50,3]
    k = 4

    ans = Solution()
    print(ans.findMaxAverage(nums, k))