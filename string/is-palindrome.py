from collections import Stack

class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) < 2:
            return True
        left = 0
        right = len(s) - 1
        while left < right:
            if not s[left].isalnum():
                left += 1
                continue
            if not s[right].isalnum():
                right -= 1
                continue
            print("s[left].lower()  = {} and s[right].lower() = {}".format(s[left].lower(), s[right].lower()))
            if s[left].lower() != s[right].lower():
                return False
            else:
                left += 1
                right -= 1
        return True


print(Solution().isPalindrome("A man, a plan, a canal: Panama"))