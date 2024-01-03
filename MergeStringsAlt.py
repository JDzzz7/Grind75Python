class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        mergedString = []
        i = 0
        while len(word1) > i or len(word2) > i:
            if len(word1) > i:
                mergedString.append(word1[i])
            if len(word2) > i:
                mergedString.append(word2[i])
            i += 1
        mergedString =  "".join(mergedString)
        return mergedString
    
if __name__ == '__main__':
    word1 = "ab"
    word2 = "pqrs"
    solution = Solution()
    print(solution.mergeAlternately(word1, word2))
        