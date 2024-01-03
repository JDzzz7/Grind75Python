class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        maxCandies = 0
        result = []
        for i in candies:
            if i > maxCandies:
                maxCandies = i
        for i in candies:
            if (i + extraCandies) >= maxCandies:
                result.append(True)
            else:
                result.append(False)
        return result
    
if __name__ == '__main__':
    candies = [2,3,5,1,3]
    extraCandies = 3
    solution = Solution()
    print(solution.kidsWithCandies(candies, extraCandies))