class Solution:
    def maxArea(self, height: list[int]) -> int:
        maxWater = 0
        currWater = 0

        start = 0
        end = len(height)-1

        while start < end:
            if height[start] <= height[end]:
                lowerBound = height[start]
            else:
                lowerBound = height[end]
            currWater = lowerBound * (end - start)
            if currWater > maxWater:
                maxWater = currWater

            if height[start] <= height[end]:
                start += 1
            else:
                end -= 1
            
        return maxWater
    
if __name__ == '__main__':
    height = [1,8,6,2,5,4,8,3,7]
    solution = Solution()
    print(solution.maxArea(height))
            

