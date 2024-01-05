class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        goal = len(s)
        anchor = 0

        if s == "":
            return True

        for traveller in t:
            if traveller == s[anchor]:
                goal -= 1
                if goal == 0:
                    return True
                if (anchor+1) < len(s):
                    anchor += 1
        return False

if __name__ == '__main__':
    s = "abc"
    t = "ahbgdc"
    solution = Solution()
    print(solution.isSubsequence(s, t))