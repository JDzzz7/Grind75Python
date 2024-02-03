class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = 'aeiou'
        numV = 0
        
        for letter in s[:k]:
            if letter in vowels:
                numV += 1
            maxV = numV

        for i in range(k, len(s)):
            # 3-3 if k was 3
            if s[i-k] in vowels:
                numV -= 1
            if s[i] in vowels:
                numV += 1
            maxV = max(numV, maxV)

        return maxV