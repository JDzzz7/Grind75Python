class Solution:
    def reverseWords(self, s: str) -> str:
        strings = s.split()
        start = 0
        end = len(strings)-1

        while start < end:
            strings[start], strings[end] = strings[end], strings[start]
            start += 1
            end -= 1

        return " ".join(strings)

if __name__ == '__main__':
    s = "the sky is blue"
    solution = Solution()
    print(solution.reverseWords(s))