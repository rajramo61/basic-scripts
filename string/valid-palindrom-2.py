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
        """
        Brute Force solution failed
        :param s:
        :return:
        """
        def validMyPalindrome(s: str) -> bool:
            if s is None or len(s) < 1:
                return True
            left = 0
            right = len(s) - 1

            while left < right:
                if s[left] == s[right]:
                    left += 1
                    right -= 1
                else:
                    return False
            return True

        if validMyPalindrome(s):
            return True
        left = 0
        right = len(s) - 1
        while left < right:
            input = s
            if left < 1:
                input = input[left + 1:]
            else:
                input = input[0: left] + input[left + 1:]
            if validMyPalindrome(input):
                return True
            else:
                input = s
                if right == len(s) - 1:
                    input = input[0: left + 1] + input[left + 1: right]
                else:
                    input = input[0: left + 1] + input[left + 1: right] + input[right + 1:]
                if validMyPalindrome(input):
                    return True
                else:
                    left += 1
                    right -= 1
        return False

