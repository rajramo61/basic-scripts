# Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.
#
# Example 1:
# Input: "aba"
# Output: True
# Example 2:
# Input: "abca"
# Output: True
# Explanation: You could delete the character 'c'.
# Note:
# The string will only contain lowercase characters a-z. The maximum length of the string is 50000.


class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalindrom(input):
            if s is None or len(input) < 1:
                return True
            l = 0
            r = len(input) - 1

            while l < r:
                if input[l] == input[r]:
                    l += 1
                    r -= 1
                else:
                    return False
            return True

        def checkReduceCheck(input):
            if len(input) < 2:
                return True
            left = 0
            right = len(input) - 1
            if input[left] == input[right]:
                if len(input) == 2 or len(input) == 3:
                    return True
                return checkReduceCheck(input[left + 1: right])
            else:
                if isPalindrom(input[left: right]):
                    return True
                else:
                    return isPalindrom(input[left + 1: right + 1])

        return checkReduceCheck(s)

