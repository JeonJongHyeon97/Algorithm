import sys

input = sys.stdin.readline

def longestPalindrome(s: str) -> str:
    def expand(left: int, right: int) -> str:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left+1:right]
    result = ''
    if len(s) <= 1 or s==s[::-1]:
        return s
    for i in range(len(s)):
        result = max(result, expand(i, i+1), expand(i, i+2), key=len)
    return result


print(longestPalindrome(input().rstrip()))