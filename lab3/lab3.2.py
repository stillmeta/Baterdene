class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        if len(s) < 2:
            return ""

        valid = True
        for i in range(len(s)):
            if s[i].islower() and s[i].upper() in s:
                continue
            elif s[i].isupper() and s[i].lower() in s:
                continue
            else:
                valid = False
                break

        if valid:
            return s

        left = self.longestNiceSubstring(s[:i])
        right = self.longestNiceSubstring(s[i+1:])

        if len(left) >= len(right):
            return left
        else:
            return right

input_string = input("Enter the string: ")
solution = Solution()
result = solution.longestNiceSubstring(input_string)
print(f"The longest nice substring is: '{result}'")