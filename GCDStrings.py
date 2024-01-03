import math

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if (str1 + str2) == (str2 + str1):
            return str1[:math.gcd(len(str1), len(str2))]
        else:
            return ""
        
if __name__ == '__main__':
    str1 = "ABABAB"
    str2 = "ABAB"
    answer = Solution()
    print(answer.gcdOfStrings(str1, str2))
    