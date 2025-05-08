class Solution:
    def lengthOfLastWord(self, s):
        words = s.strip().split()
        return len(words[-1])

sol = Solution()
s = "Hello World"
print(sol.lengthOfLastWord(s))  # Output:  