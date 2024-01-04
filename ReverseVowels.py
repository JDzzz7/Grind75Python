class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set('AEIOUaeiou')
        outputStr = list(s)
        start = 0
        end = len(s)-1

        while start < end:
            while start < end and outputStr[start] not in vowels:
                start += 1
            while start < end and outputStr[end] not in vowels:
                end -= 1
            outputStr[start] = s[end]
            outputStr[end] = s[start]

            start += 1
            end -= 1
            
        return "".join(outputStr)
    
if __name__ == "__main__":
    s = "leetcode"
    solution = Solution()
    print(solution.reverseVowels(s))
