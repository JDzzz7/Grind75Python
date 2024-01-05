class Solution:
    def compress(self, chars: list[str]) -> int:
        i = 0
        ans = 0

        while i < len(chars):
            letter = chars[i]
            count = 0
            while i < len(chars) and chars[i] == letter:
                i += 1
                count += 1
            chars[ans] = letter
            ans += 1

            if count > 1:
                s = str(count)
                for c in s:
                    chars[ans] = c
                    ans += 1

        return ans
    
if __name__ == '__main__':
    chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
    solution = Solution()
    print(solution.compress(chars))
